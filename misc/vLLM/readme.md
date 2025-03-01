# vLLM

vLLM is a fast and easy-to-use library for LLM inference and serving.

github地址: https://github.com/vllm-project/vllm  
官方文档: https://docs.vllm.ai/  

要求：
1. OS: Linux
2. Python: 3.9 – 3.12

安装：
```bash
pip install vllm
```

使用modelscope下载模型：
```bash
pip install modelscope
export VLLM_USE_MODELSCOPE=True
```

如果使用cuda，可能需要安装这个：
```bash
sudo apt install nvidia-cuda-toolkit
```

指定模型，启动一个提供OpenAI API的服务：
```bash
vllm serve Qwen/Qwen2.5-1.5B-Instruct
```

报错了，可能CPU或者GPU不支持，还不知道怎么解决  
```log
INFO 03-01 20:22:48 __init__.py:211] No platform detected, vLLM is running on UnspecifiedPlatform
INFO 03-01 20:22:49 api_server.py:912] vLLM API server version 0.7.3
INFO 03-01 20:22:49 api_server.py:913] args: Namespace(subparser='serve', model_tag='Qwen/Qwen2.5-1.5B-Instruct', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='Qwen/Qwen2.5-1.5B-Instruct', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=0, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.9, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, max_num_seqs=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=None, qlora_adapter_name_or_path=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', generation_config=None, override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, additional_config=None, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, dispatch_function=<function ServeSubcommand.cmd at 0x7f018b8c76d0>)
INFO 03-01 20:22:49 api_server.py:209] Started engine process with PID 6194
Traceback (most recent call last):
  File "/home/hello/venv/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/home/hello/venv/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 73, in main
    args.dispatch_function(args)
  File "/home/hello/venv/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 34, in cmd
    uvloop.run(run_server(args))
  File "/home/hello/venv/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/home/hello/venv/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/home/hello/venv/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 947, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/home/hello/venv/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 139, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/home/hello/venv/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 220, in build_async_engine_client_from_engine_args
    engine_config = engine_args.create_engine_config()
  File "/home/hello/venv/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 1126, in create_engine_config
    device_config = DeviceConfig(device=self.device)
  File "/home/hello/venv/lib/python3.10/site-packages/vllm/config.py", line 1660, in __init__
    raise RuntimeError("Failed to infer device type")
RuntimeError: Failed to infer device type
INFO 03-01 20:22:56 __init__.py:211] No platform detected, vLLM is running on UnspecifiedPlatform
ERROR 03-01 20:22:56 engine.py:400] Failed to infer device type
ERROR 03-01 20:22:56 engine.py:400] Traceback (most recent call last):
ERROR 03-01 20:22:56 engine.py:400]   File "/home/hello/venv/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
ERROR 03-01 20:22:56 engine.py:400]     engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
ERROR 03-01 20:22:56 engine.py:400]   File "/home/hello/venv/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 119, in from_engine_args
ERROR 03-01 20:22:56 engine.py:400]     engine_config = engine_args.create_engine_config(usage_context)
ERROR 03-01 20:22:56 engine.py:400]   File "/home/hello/venv/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 1126, in create_engine_config
ERROR 03-01 20:22:56 engine.py:400]     device_config = DeviceConfig(device=self.device)
ERROR 03-01 20:22:56 engine.py:400]   File "/home/hello/venv/lib/python3.10/site-packages/vllm/config.py", line 1660, in __init__
ERROR 03-01 20:22:56 engine.py:400]     raise RuntimeError("Failed to infer device type")
ERROR 03-01 20:22:56 engine.py:400] RuntimeError: Failed to infer device type
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/hello/venv/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 402, in run_mp_engine
    raise e
  File "/home/hello/venv/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
    engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
  File "/home/hello/venv/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 119, in from_engine_args
    engine_config = engine_args.create_engine_config(usage_context)
  File "/home/hello/venv/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 1126, in create_engine_config
    device_config = DeviceConfig(device=self.device)
  File "/home/hello/venv/lib/python3.10/site-packages/vllm/config.py", line 1660, in __init__
    raise RuntimeError("Failed to infer device type")
RuntimeError: Failed to infer device type
```
