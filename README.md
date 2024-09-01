# 🌟 sentiment_analysis_with_LLM 🌟
Implement LLM for analyzing sentiment from text message

# 🚀 Build env
``` bash
$ docker build -f docker/Dockerfile -t sentiment_analysis_with_llm:latest .
```

# 🚀 Start env
``` bash
$ docker run -it --net=host --rm -v $(pwd):/sentiment_analysis_with_LLM sentiment_analysis_with_llm:latest /bin/bash
```
# 💻 Start notebook
``` bash
python3 -m notebook --allow-root
```