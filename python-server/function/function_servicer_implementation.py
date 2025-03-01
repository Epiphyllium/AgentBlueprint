import json
import logging

import pandas as pd

import message.proto.dataIndexGen_pb2
import message.proto.functionDistribute_pb2_grpc
from prompt_template import prompt_template, response_format_gen, system_template
from ops.jsonify_data import parse_json_list
from ops.pipe_util import get_llm_op, get_prompt
from util.service_config import ServiceConfig

logger = logging.getLogger()
config = ServiceConfig()
config.embedding_device = 'cuda'

class APMFunctionsServiceServicer(object):
    """Internal Python Service to distribute the apm request to individual functions
    """
    def InsertActionWithObservation(self, request, context):
        prompt_args = {
            "system": system_template.gpt_system_prompt,
            "context": request.text,
            "prompt": request.prompt,
            "response": response_format_gen.insert_action_with_observation_response
        }
        prompt_formatter = get_prompt(prompt_template.default_prompt)
        llm_caller = get_llm_op(config=ServiceConfig())
        # run pipeline
        formatted_prompt = prompt_formatter(prompt_args)
        result = llm_caller(
            formatted_prompt,
        )
        try:
            data = json.loads(result)
        except json.JSONDecodeError:
            logger.error("JSONDecodeError: Failed to parse JSON data. Source data: %s", result)
            data = None

        action_list = message.proto.dataIndexGen_pb2.ActionList()
        if data is None:
            return action_list
        df = pd.json_normalize(data)
        for index, row in df.iterrows():
            action = message.proto.dataIndexGen_pb2.Action(
                action_description=row["action_description"],
                duration=row["duration"],
                start_time=row["start_time"],
                end_time=row["end_time"],
                emoji=message.proto.dataIndexGen_pb2.EmojiData(
                    emoji_description=row["emoji.emoji_description"],
                    emoji_unicode=row["emoji.emoji_unicode"],
                ),
            )
            action_list.action_list.append(action)

        return action_list


    def ActionFormatter(self, request, context):
        from ops.action_formatter_handler import ActionFormatterHandler
        response = ActionFormatterHandler(request)
        return response
