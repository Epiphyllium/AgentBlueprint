package tools

import (
	"fmt"
	"os"
)

func protoGen(conf *YamlConfig) {
	f, err := os.Create("message/protoData/dataIndexGen.proto")
	if err != nil {
		fmt.Println(err)
		return
	}
	f.WriteString("syntax = \"proto3\";\n")
	f.WriteString("package protoData;\n")
	f.WriteString("option go_package = \"golang-client/message\";\n")
	f.WriteString("// --------------InternalData--------\n")
	sortedInternalData := SortData(conf.InternalData)
	for _, data := range sortedInternalData {
		name := data.Key
		f.WriteString("message " + name + " {\n")
		for propname, detail_property := range data.Value.Property {
			f.WriteString("	" + detail_property.Type + " " + ToSnakeCase(propname) + " = " + fmt.Sprint(detail_property.Index) + ";\n")
		}
		f.WriteString("}\n")
	}
	f.WriteString("// --------------SystemData--------\n")
	sortedSystemData := SortData(conf.SystemData)
	for _, data := range sortedSystemData {
		name := data.Key
		f.WriteString("message " + name + " {\n")
		for propname, detail_property := range data.Value.Property {
			f.WriteString("	" + detail_property.Type + " " + ToSnakeCase(propname) + " = " + fmt.Sprint(detail_property.Index) + ";\n")
		}
		f.WriteString("}\n")
		f.WriteString("message " + name + "List {\n")
		f.WriteString("	repeated " + name + " " + ToSnakeCase(name) + "_list" + " = 1;\n")
		f.WriteString("}\n")
	}
	f.WriteString("// --------------ExternalData--------\n")
	sortedExternalData := SortData(conf.ExternalData)
	for _, data := range sortedExternalData {
		name := data.Key
		f.WriteString("message " + name + " {\n")
		for propname, detail_property := range data.Value.Property {
			f.WriteString("	" + detail_property.Type + " " + ToSnakeCase(propname) + " = " + fmt.Sprint(detail_property.Index) + ";\n")
		}
		f.WriteString("}\n")
	}
	f.Close()

}
