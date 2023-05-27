from __future__ import annotations

import torch
import requests
import numpy as np
from typing import List, Optional, Union

import utils
from logger import logger
from modeling.inference_model import (
    GenerationResult,
    GenerationSettings,
    InferenceModel,
    ModelCapabilities,
)

model_backend_name = "Read Only"

class BasicAPIException(Exception):
    """To be used for errors when using the Basic API as an interface."""


class model_backend(InferenceModel):
    def __init__(self) -> None:
        super().__init__()

        # Do not allow API to be served over the API
        self.capabilties = ModelCapabilities(api_host=False)
        self.tokenizer = self._tokenizer()
        self.model = None
        self.model_name = "Read Only"
    
    def is_valid(self, model_name, model_path, menu_path):
        return model_name == "ReadOnly"
    
    def get_requested_parameters(self, model_name, model_path, menu_path, parameters = {}):
        requested_parameters = []
        return requested_parameters
        
    def set_input_parameters(self, parameters):
        return

    def unload(self):
        utils.koboldai_vars.noai = False

    def _initialize_model(self):
        return
    
    class _tokenizer():
        def __init__(self):
            self._koboldai_header = []
        def decode(self, _input):
            return ""
        def encode(self, input_text):
            return []

    def _load(self, save_model: bool = False, initial_load: bool = False) -> None:
        self.tokenizer = self.tokenizer
        self.model = None
        utils.koboldai_vars.noai = True

    def _raw_generate(
        self,
        prompt_tokens: Union[List[int], torch.Tensor],
        max_new: int,
        gen_settings: GenerationSettings,
        single_line: bool = False,
        batch_count: int = 1,
        seed: Optional[int] = None,
        **kwargs,
    ):
        return GenerationResult(
            model=self,
            out_batches=np.array([]),
            prompt=prompt_tokens,
            is_whole_generation=True,
            single_line=single_line,
        )
