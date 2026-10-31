# -*- coding: utf-8 -*-
# 格式: full_name -> (stack分组, 标签|分隔, 中文简介, 适用场景)
A = {
"codecrafters-io/build-your-own-x": ("学习资源", "编程实战|教程合集|造轮子",
  "手把手教你从零复刻 Git、Docker、Redis、数据库、编译器 等经典技术的学习项目合集。",
  "想通过亲手造轮子真正理解底层原理，而不是只会调 API 的开发者。"),

"sindresorhus/awesome": ("学习资源", "清单|资源索引|Awesome",
  "一个索引式的超大型清单库，汇总编程、计算机科学、硬件、商业等各类优质资源列表。",
  "想系统查找某个领域的资料时，先来这里定位对应的 awesome 子清单。"),

"public-apis/public-apis": ("学习资源", "免费API|清单|开发资源",
  "收录上千个免费开放 API 的清单，按领域分类，并标注是否需要密钥与鉴权方式。",
  "做 Demo、练手项目，或寻找第三方数据源时快速定位可用 API。"),

"freeCodeCamp/freeCodeCamp": ("学习资源", "免费课程|编程教育|TypeScript",
  "全球最大的免费编程学习平台源码，包含数千小时交互式课程与多项认证体系。",
  "零基础自学编程；或作为在线教学平台的架构参考。"),

"morluto/rea": ("安全", "逆向工程|AI Agent|二进制分析",
  "用 AI Agent 驱动逆向工程的工具链，可从应用行为一路下钻到原生二进制层面。",
  "安全研究、协议逆向、以及对闭源程序做行为分析。"),

"EbookFoundation/free-programming-books": ("学习资源", "免费书籍|多语言|清单",
  "社区维护的免费编程书籍清单，覆盖几十种语言与上百个技术方向，持续更新。",
  "想找免费电子书系统学习时，按语言与主题精准检索。"),

"openclaw/openclaw": ("AI / 大模型", "AI助手|跨平台|个人助理",
  "主打「真正能做事」的个人 AI 助理，支持任意操作系统与平台，强调数据自主可控。",
  "想把日常任务交给 Agent 自动执行的个人用户与自动化爱好者。"),

"donnemartin/system-design-primer": ("学习资源", "系统设计|面试|架构",
  "系统设计面试的系统化学习仓库，讲解大规模系统设计思路，并附 Anki 记忆卡。",
  "准备后端/架构岗面试，或需要补齐分布式系统设计知识。"),

"nilbuild/developer-roadmap": ("学习资源", "学习路线|前端|后端|DevOps",
  "交互式开发者成长路线图，用知识图谱串联前端、后端、DevOps、AI 等方向的技能点。",
  "不确定下一步该学什么时，按路线图定位自己的知识缺口。"),

"jwasham/coding-interview-university": ("学习资源", "计算机基础|面试|学习计划",
  "一份完整的计算机科学自学计划，从数据结构到操作系统逐项列出学习材料与目标。",
  "非科班转行，或想系统补齐计算机基础后再冲击大厂面试。"),

"awesome-selfhosted/awesome-selfhosted": ("DevOps / 云原生", "自托管|开源软件|清单",
  "可自建部署的免费网络服务与应用清单，涵盖网盘、笔记、监控、媒体、协作等场景。",
  "想用 Docker 搭私有云服务、替代商业 SaaS 的用户。"),

"vinta/awesome-python": ("Python", "Python|库推荐|清单",
  "Python 生态最全的库与工具清单，按用途分类回答「做 X 该用什么库」。",
  "技术选型时快速对比方案，或系统了解某个 Python 方向的成熟生态。"),

"obra/superpowers": ("AI / 大模型", "Agent Skills|开发方法论|AI编程",
  "面向 AI Agent 的技能框架与软件开发方法论，用结构化技能包驱动完整研发流程。",
  "使用 Claude Code 等编码 Agent，希望规范其工作方式与产出质量。"),

"mattpocock/skills": ("AI / 大模型", "Agent Skills|工程实践",
  "工程师实战向的 Agent Skills 合集，内容直接取自作者日常使用的 .agents 目录。",
  "给编码 Agent 配置可复用的工程技能，提升代码产出稳定性。"),

"affaan-m/ECC": ("AI / 大模型", "Agent优化|记忆|MCP",
  "Agent 运行框架的性能优化系统，整合技能、直觉、记忆、安全与研究优先的开发流程。",
  "重度使用 Claude Code / Codex，需要管理上下文与长期记忆的开发者。"),

"practical-tutorials/project-based-learning": ("学习资源", "项目实战|教程|多语言",
  "以做项目为主线整理的学习教程清单，覆盖 C++、Go、JavaScript、Python 等语言。",
  "不想只看视频，希望通过动手完成一个完整项目来掌握技术。"),

"deepseek-ai/deepseek-harness": ("AI / 大模型", "DeepSeek|插件化|Agent",
  "DeepSeek 官方 Harness 框架，以「一切皆插件」为设计理念组织 Agent 能力。",
  "希望在 DeepSeek 模型之上构建可扩展 Agent 应用的开发者。"),

"NousResearch/hermes-agent": ("AI / 大模型", "AI Agent|Python|可成长",
  "可随使用不断进化的开源 AI Agent，内置工具调用、多模型适配与会话记忆。",
  "搭建个人或团队 Agent，希望它能积累经验并持续变强。"),

"trimstray/the-book-of-secret-knowledge": ("DevOps / 云原生", "运维|清单|速查",
  "面向运维与工程师的效率知识合集：手册、速查表、单行命令、CLI/Web 工具清单。",
  "排查服务器问题、或系统整理自己的命令行工具箱。"),

"torvalds/linux": ("C / C++", "Linux内核|操作系统|系统编程",
  "Linux 内核官方源码树，是现代操作系统最核心的开源实现，驱动着绝大多数服务器。",
  "内核开发、驱动编写，或想深入理解操作系统调度与内存管理。"),

"react/react": ("React", "React|UI库|组件化",
  "构建 Web 与原生用户界面的声明式组件库，组件化开发的行业事实标准。",
  "几乎所有中大型前端项目，以及基于 React Native 的跨端应用。"),

"multica-ai/andrej-karpathy-skills": ("AI / 大模型", "CLAUDE.md|提示词|LLM",
  "单文件 CLAUDE.md 规则集，提炼 Karpathy 对 LLM 编程踩坑的观察来约束编码 Agent。",
  "想让 Claude Code 少犯低级错误、输出更贴近资深工程师习惯。"),

"TheAlgorithms/Python": ("Python", "算法|教学|Python",
  "用 Python 实现各类经典算法的教学仓库，每个算法都配有可运行示例与说明。",
  "学习算法实现细节，或准备算法面试时对照阅读。"),

"anomalyco/opencode": ("AI / 大模型", "编码Agent|终端|开源",
  "开源终端编码 Agent，可在本地理解代码库并直接执行改代码、跑命令等开发任务。",
  "想要 Claude Code 的开源替代品，在终端里用 AI 干活。"),

"vuejs/vue": ("Vue", "Vue|渐进式|JavaScript",
  "Vue 2 官方源码仓库，渐进式 JavaScript 框架，以数据驱动视图与组件化开发著称。",
  "维护 Vue 2 存量项目；新项目建议直接上 Vue 3（vuejs/core）。"),

"ossu/computer-science": ("学习资源", "计算机科学|自学|课程体系",
  "免费的计算机科学自学路径，按学期组织课程，对标名校 CS 培养方案。",
  "想不花钱系统学完一整套计算机本科核心课程。"),

"n8n-io/n8n": ("DevOps / 云原生", "工作流自动化|AI|低代码",
  "可视化工作流自动化平台，原生集成 AI 能力，内置 400+ 服务连接器，可自托管。",
  "把多个 SaaS、内部 API 与 AI 模型串成自动流程，替代 Zapier。"),

"DigitalPlatDev/FreeDomain": ("DevOps / 云原生", "免费域名|DNS|建站",
  "提供免费域名注册与 DNS 学习资源的项目，面向个人建站与网络实验。",
  "搭个人博客或小项目，想要一个零成本域名。"),

"yt-dlp/yt-dlp": ("Python", "视频下载|命令行|Python",
  "功能强大的命令行音视频下载器，支持上千个站点，是 youtube-dl 的活跃继任分支。",
  "需要批量下载、转码或归档网络音视频内容。"),

"tensorflow/tensorflow": ("AI / 大模型", "深度学习|机器学习|C++",
  "Google 开源的全流程机器学习框架，覆盖模型训练、分布式训练到移动端推理部署。",
  "工业级模型训练与线上服务，或需要成熟生态的生产级项目。"),

"firecrawl/firecrawl": ("AI / 大模型", "爬虫|AI|Markdown",
  "为 AI Agent 提供网页数据的抓取服务，可把任意站点转换成干净的 Markdown。",
  "给 RAG 或 Agent 喂实时网页内容，免去自己写解析规则。"),

"trekhleb/javascript-algorithms": ("学习资源", "算法|数据结构|JavaScript",
  "用 JavaScript 实现常用算法与数据结构，每份代码都附带讲解和延伸阅读链接。",
  "前端工程师补算法基础、准备技术面试。"),

"ultraworkers/claw-code": ("AI / 大模型", "Agent|Rust|实验项目",
  "由 Agent 自主管理维护的 Rust 实验项目，全程无人工干预完成开发与迭代。",
  "作为案例研究，观察 AI 自主开发目前能达到什么程度。"),

"microsoft/vscode": ("开发工具", "编辑器|Electron|TypeScript",
  "Visual Studio Code 官方源码，当前最流行的跨平台轻量代码编辑器。",
  "想做编辑器二次开发，或基于它搭建 Web IDE 底座。"),

"microsoft/markitdown": ("Python", "文档转换|Markdown|Python",
  "微软出品的文档转 Markdown 工具，支持 PDF、Word、PPT、Excel 等常见办公格式。",
  "把办公文档批量转成 Markdown 喂给 LLM，或构建知识库预处理管线。"),

"avelino/awesome-go": ("Go", "Go|库推荐|清单",
  "Go 语言生态的精选框架、库与软件清单，按领域分类持续维护。",
  "Go 项目选型时快速找到成熟稳定的第三方库。"),

"ohmyzsh/ohmyzsh": ("开发工具", "Shell|zsh|终端美化",
  "zsh 配置管理框架，内置 300+ 插件与主题，让终端开箱即用又好看。",
  "想快速把终端配置得顺手好用，又不想手写一堆配置文件。"),

"Significant-Gravitas/AutoGPT": ("AI / 大模型", "自主Agent|AI|Python",
  "自主 AI Agent 的开创性项目，让模型自行拆解目标、调用工具并持续执行任务。",
  "研究自主 Agent 架构，或做多步骤任务自动化的原型验证。"),

"jackfrued/Python-100-Days": ("学习资源", "Python|教程|中文",
  "《Python-100 天从新手到大师》中文教程，从语法基础一路讲到 Django 与数据分析。",
  "中文零基础学 Python，希望按天推进有明确路径。"),

"CyC2018/CS-Notes": ("学习资源", "面试|计算机基础|中文",
  "技术面试必备基础知识笔记，覆盖算法、操作系统、网络、数据库与系统设计。",
  "校招或社招前突击复习计算机基础考点。"),

"521xueweihan/HelloGitHub": ("学习资源", "开源推荐|月刊|中文",
  "每月分享 GitHub 上有趣、入门级开源项目的月刊，全部附有中文介绍。",
  "想持续发现好玩的项目，又不想自己在 GitHub 上大海捞针。"),

"anthropics/skills": ("AI / 大模型", "Agent Skills|Anthropic|官方",
  "Anthropic 官方的 Agent Skills 公开仓库，提供可直接复用的技能定义。",
  "为 Claude 系列 Agent 扩展结构化能力与领域知识。"),

"ollama/ollama": ("AI / 大模型", "本地大模型|LLM|Go",
  "一条命令在本地跑开源大模型的工具，支持 DeepSeek、Qwen、Gemma 等主流模型。",
  "想离线使用大模型，或做不依赖云 API 的本地 AI 应用。"),

"getify/You-Dont-Know-JS": ("学习资源", "JavaScript|书系|语言原理",
  "《你不知道的 JavaScript》系列书籍源码，深入讲解作用域、闭包、异步等语言机制。",
  "想真正吃透 JS 语言机制，而不只是会写业务代码。"),

"DietrichGebert/ponytail": ("AI / 大模型", "Agent Skills|代码质量",
  "让 AI Agent 以「最懒的资深工程师」思维工作，优先选择不写代码的解法。",
  "抑制 Agent 过度设计、减少无谓代码量与维护负担。"),

"flutter/flutter": ("移动端", "Flutter|跨平台|Dart",
  "Google 的跨平台 UI 框架，一套 Dart 代码构建 iOS、Android、Web 与桌面应用。",
  "小团队要同时上线多端 App，且希望视觉与动效保持一致。"),

"github/gitignore": ("开发工具", "Git|模板|配置",
  "官方维护的 .gitignore 模板集合，覆盖主流语言、框架与 IDE。",
  "新建仓库时快速拿到一份合适的忽略规则。"),

"f/prompts.chat": ("AI / 大模型", "提示词|ChatGPT|社区",
  "原 Awesome ChatGPT Prompts，社区共享与收藏提示词的平台，支持自托管部署。",
  "找不到提示词灵感，或团队想统一维护一套提示词库。"),

"twbs/bootstrap": ("前端其他", "CSS框架|响应式|Sass",
  "最流行的 HTML/CSS/JS 前端框架，提供成熟的响应式栅格系统与组件库。",
  "快速搭管理后台、落地页，不想自己从零写设计系统。"),

"huggingface/transformers": ("AI / 大模型", "模型库|深度学习|多模态",
  "Hugging Face 的模型定义框架，统一加载文本、视觉、音频与多模态 SOTA 模型。",
  "直接调用预训练模型做推理或微调，免去手写网络结构。"),

"msitarzewski/agency-agents": ("AI / 大模型", "Agent|角色分工|工作流",
  "把一整套「AI 代理公司」拆成不同角色的 Agent：前端、社区运营、创意、现实校验等。",
  "需要多个角色协作完成产品、内容或运营任务的场景。"),

"AUTOMATIC1111/stable-diffusion-webui": ("AI / 大模型", "Stable Diffusion|图像生成|Gradio",
  "Stable Diffusion 最流行的 Web 操作界面，支持文生图、图生图与插件扩展。",
  "本地跑 SD 模型做 AI 绘画、批量出图与 LoRA 调试。"),

"jlevy/the-art-of-command-line": ("学习资源", "命令行|Linux|速查",
  "一页纸讲透命令行精髓的指南，涵盖 bash 技巧、文本处理与系统排查。",
  "想从「会用几条命令」进阶到熟练驾驭 Shell 的开发者。"),

"langgenius/dify": ("AI / 大模型", "Agent平台|RAG|工作流",
  "可视化构建 Agentic 工作流与 RAG 管线的平台，支持多云模型与自托管部署。",
  "企业快速把 AI 应用从原型推进到生产，统一管理工作流与知识库。"),

"Snailclimb/JavaGuide": ("Java", "Java|面试|后端",
  "Java 与后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发与 AI 应用开发。",
  "Java 后端求职复习，或系统梳理自己的后端知识体系。"),

"open-webui/open-webui": ("AI / 大模型", "LLM界面|Ollama|自托管",
  "可自托管的 AI 对话界面，兼容 Ollama 与 OpenAI 接口，支持多用户与知识库。",
  "给团队搭一个私有的 ChatGPT，统一管理模型与对话数据。"),

"langflow-ai/langflow": ("AI / 大模型", "可视化编排|Agent|低代码",
  "基于节点画布构建与部署 AI Agent 和自动化流程的低代码平台。",
  "非算法背景的开发者快速拼装 AI 应用原型。"),

"anthropics/claude-code": ("AI / 大模型", "编码Agent|终端|Anthropic",
  "Anthropic 官方终端编码 Agent，能读懂整个代码库并执行日常开发任务。",
  "在命令行里让 AI 直接改代码、跑测试、整理提交。"),

"Genymobile/scrcpy": ("开发工具", "安卓投屏|设备控制|C",
  "把 Android 设备画面投到电脑并直接用键鼠控制，无需 root，延迟极低。",
  "演示手机操作、录屏，或用大屏和实体键盘高效操作安卓设备。"),

"farion1231/cc-switch": ("开发工具", "多Agent管理|桌面应用|Rust",
  "跨平台桌面工具，统一管理 Claude Code、Codex、OpenCode 等多个编码 Agent 的配置。",
  "同时使用多个 AI 编码工具，需要一处切换与集中管理。"),

"langchain-ai/langchain": ("AI / 大模型", "Agent框架|LLM|Python",
  "Agent 工程平台与开发框架，提供模型、工具、检索与编排的标准化抽象层。",
  "构建生产级 LLM 应用，需要成熟的链路编排与生态集成能力。"),

"airbnb/javascript": ("学习资源", "JavaScript|代码规范|ESLint",
  "Airbnb 的 JavaScript 编码风格指南，前端事实上的规范参考标准。",
  "团队要统一代码风格，或配置一份有依据的 ESLint 规则。"),

"x1xhlol/system-prompts-and-models-of-ai-tools": ("AI / 大模型", "系统提示词|逆向|研究",
  "收集各家 AI 产品（Cursor、Devin、v0 等）系统提示词与内部模型信息的资料库。",
  "研究商业 AI 产品如何设计提示词、工具调用与输出约束。"),

"Comfy-Org/ComfyUI": ("AI / 大模型", "扩散模型|节点式|本地推理",
  "节点式图形界面的扩散模型工作台，可精细控制生成流程，本地推理速度极快。",
  "需要精确控制 AI 绘图流程，或搭建可复用的生成管线。"),

"github/spec-kit": ("AI / 大模型", "规格驱动|SDD|工具包",
  "GitHub 官方的规格驱动开发（SDD）工具包，把需求文档转化为 Agent 可执行的规格。",
  "想让 AI 编码前先产出清晰规格，减少返工与需求跑偏。"),

"Shubhamsaboo/awesome-llm-apps": ("AI / 大模型", "LLM应用|RAG|示例",
  "100+ 个可直接运行的 AI Agent、Agent Skills 与 RAG 应用示例合集。",
  "想找能跑起来的 LLM 应用模板，改一改就能用于自己的场景。"),

"vercel/next.js": ("React", "React|SSR|全栈",
  "React 全栈框架，内置文件路由、服务端渲染、API 路由与增量静态生成。",
  "做需要 SEO 的官网、电商、内容站，以及一体化全栈 Web 应用。"),

"yangshun/tech-interview-handbook": ("学习资源", "面试|算法|行为面",
  "为忙碌工程师准备的面试资料：算法题、行为面试、简历撰写与 offer 谈判。",
  "时间有限、想高效准备一场技术面试。"),

"nextlevelbuilder/ui-ux-pro-max-skill": ("AI / 大模型", "Agent Skills|UI/UX|设计",
  "给 AI 编码 Agent 注入专业 UI/UX 设计能力的设计智能技能包。",
  "让 Agent 生成的前端页面不只是能跑，而是真的好看。"),

"iptv-org/iptv": ("前端其他", "IPTV|直播源|m3u",
  "全球公开 IPTV 频道合集，以标准 m3u 播放列表形式维护与更新。",
  "在支持 m3u 的播放器里导入直播源，观看公开电视频道。"),

"ytdl-org/youtube-dl": ("Python", "视频下载|Python|命令行",
  "老牌命令行视频下载工具，支持大量站点（目前主要由 yt-dlp 接棒维护）。",
  "维护依赖 youtube-dl 的老脚本，或研究下载器实现原理。"),

"ripienaar/free-for-dev": ("学习资源", "免费资源|SaaS|清单",
  "面向开发者的免费套餐清单：各类 SaaS、PaaS、IaaS 的免费额度与限制说明。",
  "个人项目想零成本上线，寻找免费的数据库、托管与 CDN。"),

"microsoft/PowerToys": ("开发工具", "Windows|效率|系统增强",
  "微软官方 Windows 效率工具集：窗口分屏、批量重命名、取色器、命令面板等。",
  "想把 Windows 调教得更顺手、日常操作更高效。"),

"Graphify-Labs/graphify": ("AI / 大模型", "知识图谱|代码分析|Agent",
  "把代码库、文档、SQL schema 与 PDF 转成可查询知识图谱的 Agent 技能。",
  "快速理解陌生大型代码库的结构、依赖与调用关系。"),

"golang/go": ("Go", "Go|编程语言|编译器",
  "Go 语言官方源码，包含编译器、运行时与标准库完整实现。",
  "学习语言实现原理，参与 Go 生态贡献，或排查运行时问题。"),

"garrytan/gstack": ("AI / 大模型", "Claude Code|工具集|工作流",
  "一套经过实战检验的 Claude Code 配置：23 个扮演 CEO、设计、QA 等角色的工具。",
  "想直接套用成熟的 AI 开发工作流，而不是自己从零摸索。"),

"harry0703/MoneyPrinterTurbo": ("AI / 大模型", "短视频|AI生成|自动化",
  "输入主题或关键词即可自动生成高清短视频，自动串联文案、配音、素材与剪辑。",
  "批量产出短视频内容，或搭建自媒体矩阵的自动化产线。"),
}
