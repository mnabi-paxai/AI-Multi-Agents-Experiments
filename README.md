# AI-Multi-Agents-Experiments - V2
_On a mission to find bugs in our current thinking about AI agents._

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#license)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)

---

## Table of Contents
- [Overview](#overview)
- [Neuro-San Studio](#neuro-san-studio)
- [Simple Agents](#simple-agents)
- [Notes & Questions](#notes--questions)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
Explorations in building and testing multi-agent systems.  
Agents are framed as **Brain (LLM)**, **Memory**, and **Tools**.  

---

## Neuro-San Studio

I tried [Neuro-San Studio](https://github.com/cognizant-ai-lab/neuro-san-studio?tab=readme-ov-file).  

<!--
I could run the examples, but I’m still working on implementing my own example for cap table updates.  
-->

---

## Simple Agents

### First AI Agent - From Futurepedia
<!--
[![Watch the video](https://img.youtube.com/vi/EH5jx5qPabU/hqdefault.jpg)](https://www.youtube.com/watch?v=EH5jx5qPabU)
-->


[![Demo Video](assets/Simple-first-AIAssistant-Hike.png)](https://www.youtube.com/watch?v=EH5jx5qPabU)

#### Summary
Gets a list of hikes in Zip Code X, gets the weather, gets my calendar, gets air quality -------> Suggets wwhat hike/run to do

#### Key points:  
- **Agents = Brain (LLM), Memory, Tools**  
- **API Requests**  
  - **GET** → pulling information  
  - **POST** → sending information  
- **API** = set of available actions or options  
- **HTTP Request** = a specific instruction to perform one of those actions/options  


#### Agent Prompts
Structure for designing an agent prompt:
- **Role** – what kind of assistant is it?  
- **Task** – what is it trying to accomplish?  
- **Input** – what data does it have access to?  
- **Tools** – which actions can it take?  
- **Constraints** – what rules should it follow?  
- **Output** – what should the final result look like? 

[Open agent-hike-prompt.txt](assets/agent-hike-prompt.txt)


<!--
<img src="assets/AgentPrompt.png" alt="Agent prompt template" width="540">
-->

#### What can go wrong?

---

### AI Blog to Podcast Agent

#### Reference

[![I Blog to Podcast Agent](assets/blog2podcast.png)](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/ai_blog_to_podcast_agent)


[AI Blog to Podcast Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/ai_blog_to_podcast_agent)


#### Summary
This is a Streamlit-based application that allows users to convert any blog post into a podcast. The app uses OpenAI's GPT-4 model for summarization, Firecrawl for scraping blog content, and ElevenLabs API for generating audio. Users simply input a blog URL, and the app will generate a podcast episode based on the blog.

#### Fix the code

[open fix_summary_blog_to_podcast_agent.md](blog2podcast/fix_summary_blog_to_podcast_agent.md)

---

### AI Data Analysis Agent

#### Reference
[AI Data Analysis Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/starter_ai_agents/ai_data_analysis_agent)


#### Summary
An AI data analysis Agent built using the Agno Agent framework and Openai's gpt-4o model. This agent helps users analyze their data - csv, excel files through natural language queries, powered by OpenAI's language models and DuckDB for efficient data processing - making data analysis accessible to users regardless of their SQL expertise.



---
---

## Notes & Questions
- Brain should be **more than an LLM**.  
- If I have a ML algorithm — should it be the brain or a tool?  

---

## Potential Applications
- **YouTube**: Find the best videos on AI agents and summarize takeaways.  
- **Podcasts**: Collect top episodes, with notes on what worked and what didn’t.  

---

## Resources

---

## Contributing
PRs welcome! Open an issue or submit a pull request if you’d like to collaborate.  

---

## License
MIT © PaxAI
