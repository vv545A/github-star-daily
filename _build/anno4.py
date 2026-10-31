# -*- coding: utf-8 -*-
A = {
"awesomedata/awesome-public-datasets": ("学习资源", "数据集|开放数据|清单",
  "按主题分类的高质量开放数据集清单，覆盖金融、地理、健康、自然语言等方向。",
  "做数据分析、训练模型时寻找公开可用的真实数据集。"),

"coder/code-server": ("开发工具", "Web IDE|远程开发|VSCode",
  "把 VS Code 跑在服务器上、浏览器直接访问的方案，随时随地连上同一开发环境。",
  "用平板或低配电脑开发，或需要统一的远程开发环境。"),

"dair-ai/Prompt-Engineering-Guide": ("AI / 大模型", "提示工程|RAG|指南",
  "提示工程系统指南，涵盖提示技巧、上下文工程、RAG 与 Agent 的理论、论文与实践。",
  "想系统提升提示词质量，而不是靠零散技巧反复试错。"),

"shareAI-lab/learn-claude-code": ("AI / 大模型", "Agent原理|教学|从零实现",
  "从 0 到 1 手写一个类 Claude Code 的 Agent Harness 教学项目。",
  "想搞懂编码 Agent 内部如何运转，并自己动手实现一个。"),

"doocs/advanced-java": ("Java", "Java进阶|分布式|面试",
  "互联网 Java 工程师进阶知识库，覆盖高并发、分布式、缓存、消息队列与微服务。",
  "Java 后端从「会写业务」迈向「懂架构」的系统补课。"),

"career-ops-hq/career-ops": ("AI / 大模型", "求职|Agent|简历匹配",
  "开源 AI 求职 Agent：扫描招聘网站，按你的简历给每个岗位打 1–5 分再决定投不投。",
  "海投效率低，想让 AI 先帮你筛掉明显不匹配的岗位。"),

"unslothai/unsloth": ("AI / 大模型", "微调|本地训练|显存优化",
  "本地运行与微调 LLM 和扩散模型的工具，显存占用低，支持 GGUF、MLX 等格式。",
  "只有一张消费级显卡，也想做模型微调与本地推理。"),

"obsproject/obs-studio": ("C / C++", "直播|录屏|推流",
  "免费开源的直播与录屏软件，支持多场景切换、多源混流与硬件编码。",
  "直播推流、课程录制、游戏录屏与画面合成。"),

"caddyserver/caddy": ("Go", "Web服务器|HTTPS|反向代理",
  "多平台 HTTP 服务器，自动申请与续期 HTTPS 证书，配置极简。",
  "需要一键上 HTTPS 的站点、反向代理与静态文件服务。"),

"elastic/elasticsearch": ("数据库 / 存储", "搜索引擎|全文检索|分布式",
  "分布式 RESTful 搜索引擎，提供全文检索、聚合分析与近实时查询能力。",
  "商品搜索、日志检索、复杂聚合统计与站内搜索。"),

"headroomlabs-ai/headroom": ("AI / 大模型", "上下文压缩|Token优化|RAG",
  "在内容进入 LLM 之前压缩工具输出、日志、文件与 RAG 片段，显著减少 token 消耗。",
  "长上下文场景下成本过高，或经常触发上下文超限。"),

"microsoft/ai-agents-for-beginners": ("AI / 大模型", "AI Agent|课程|入门",
  "微软的 18 节 AI Agent 入门课，从概念、工具调用讲到多 Agent 与 RAG。",
  "想系统学习 Agent 设计与实现，按课程循序渐进。"),

"ComposioHQ/awesome-claude-skills": ("AI / 大模型", "Agent Skills|清单|定制",
  "精选的 Claude Skills 清单与资源，用于定制 Claude 的工作流与专业能力。",
  "想给 Claude 装配现成技能，快速扩展其可用边界。"),

"AppFlowy-IO/AppFlowy": ("移动端", "知识库|Notion替代|协作",
  "AI 协作工作空间，融合文档、看板与知识库，可自托管，定位 Notion + Miro 替代。",
  "团队想要数据自主的协作工具，或需要离线可用的知识库。"),

"Asabeneh/30-Days-Of-Python": ("学习资源", "Python|30天|练习",
  "30 天 Python 挑战教程，每天一个主题配练习，从语法到 Flask 与数据分析。",
  "想用固定节奏、每天半小时把 Python 学下来。"),

"python/cpython": ("Python", "Python|解释器|语言实现",
  "Python 官方解释器源码，包含语言核心、标准库与 C 扩展接口。",
  "研究语言实现、写 C 扩展，或为 Python 本体贡献代码。"),

"tensorflow/models": ("AI / 大模型", "模型库|TensorFlow|示例",
  "TensorFlow 官方模型与示例集合，覆盖视觉、文本、语音等任务的参考实现。",
  "想找官方背书的模型实现作为项目起点。"),

"grafana/grafana": ("数据可视化", "监控看板|可观测性|可视化",
  "开源可观测性与数据可视化平台，把指标、日志、链路数据统一成可交互看板。",
  "搭建运维监控大屏，或做业务数据看板与告警。"),

"nomic-ai/gpt4all": ("AI / 大模型", "本地LLM|离线|跨平台",
  "在任意设备上本地运行开源 LLM 的方案，提供桌面客户端与 Python 接口。",
  "想离线使用大模型，且设备配置不高。"),

"tesseract-ocr/tesseract": ("C / C++", "OCR|文字识别|开源",
  "老牌开源 OCR 引擎，支持上百种语言，可训练自定义字体模型。",
  "离线批量识别图片文字，或集成到自己的软件里做识别模块。"),

"redis/redis": ("数据库 / 存储", "缓存|内存数据库|高性能",
  "内存键值数据库，支持多种数据结构、持久化与集群，是缓存与实时场景的标配。",
  "做缓存层、会话存储、排行榜与实时计数。"),

"FortAwesome/Font-Awesome": ("前端其他", "图标库|SVG|字体",
  "最常用的图标工具包，提供 SVG、字体与 CSS 多种接入方式。",
  "项目里需要一套风格统一、覆盖度高的图标。"),

"nestjs/nest": ("Node.js / TS", "Node框架|TypeScript|企业级",
  "渐进式 Node.js 框架，内置依赖注入、模块化与装饰器，架构约定清晰。",
  "团队做中大型 Node 服务，需要可维护的分层架构。"),

"ocornut/imgui": ("C / C++", "GUI库|即时模式|游戏开发",
  "无膨胀的 C++ 图形界面库，即时模式设计，几乎零依赖，易嵌入现有渲染循环。",
  "给游戏、引擎或工具做调试面板与内部工具界面。"),

"openai/openai-cookbook": ("AI / 大模型", "OpenAI|示例|最佳实践",
  "OpenAI 官方示例与指南合集，演示 API 的常见用法与工程实践。",
  "接入 OpenAI 接口时查找官方推荐写法，避免踩坑。"),

"MisterBooo/LeetCodeAnimation": ("学习资源", "LeetCode|动画|题解",
  "用动画演示 LeetCode 题目解题思路的项目，中文讲解、逐步展开。",
  "看静态题解仍然想不通，需要动态过程来理解算法。"),

"PKUFlyingPig/cs-self-learning": ("学习资源", "计算机自学|路线|中文",
  "计算机自学指南，汇总各方向的学习路线、课程与教材，中文编写。",
  "想自学计算机但面对海量资料不知如何取舍。"),

"chrislgarry/Apollo-11": ("其他", "阿波罗|汇编|历史代码",
  "阿波罗 11 号导航计算机（AGC）的原始汇编源码，航天史与软件史的活化石。",
  "对早期嵌入式软件、汇编与航天计算感兴趣的读者。"),

"sdmg15/Best-websites-a-programmer-should-visit": ("学习资源", "网站推荐|清单|工具",
  "程序员值得收藏的网站清单，涵盖学习、刷题、工具、资讯与求职。",
  "想扩充自己的技术书签库，找各类实用站点。"),

"heygen-com/hyperframes": ("AI / 大模型", "视频生成|HTML|Agent",
  "写 HTML 就能渲染成视频的框架，专为 Agent 生成视频内容而设计。",
  "需要程序化、可批量生成的营销与讲解视频。"),

"colbymchenry/codegraph": ("AI / 大模型", "代码图谱|索引|Agent",
  "预索引的代码知识图谱，随代码变更自动同步，供编码 Agent 快速检索上下文。",
  "大型仓库里让 Agent 更快定位相关代码，减少盲目搜索。"),

"hiyouga/LlamaFactory": ("AI / 大模型", "微调|LLM|统一框架",
  "统一高效的 100+ LLM 与多模态模型微调框架，支持 LoRA、全参与分布式训练。",
  "想用一套配置完成不同开源模型的微调实验。"),

"rohitg00/ai-engineering-from-scratch": ("AI / 大模型", "AI工程|课程|实战",
  "从零学 AI 工程的课程式仓库，边学边构建可交付的 AI 应用。",
  "有编程基础，想转向 AI 应用工程方向。"),

"typicode/json-server": ("Node.js / TS", "Mock API|REST|快速原型",
  "30 秒生成一套完整的假 REST API，基于一个 JSON 文件即可增删改查。",
  "前端还没接口时先跑通页面，或做教学演示。"),

"apache/superset": ("数据可视化", "BI|数据探索|SQL",
  "Apache 出品的数据可视化与探索平台，连上数据库即可拖拽生成图表与看板。",
  "企业内需要自建 BI 看板，替代高价商业 BI 工具。"),

"storytold/photocraft": ("Rust", "图片编辑|Rust|原生应用",
  "用纯 Rust 从零编写的开源照片编辑器，注重性能与原生体验。",
  "想找一个轻量、无云依赖的本地修图工具，或学习 Rust GUI 实践。"),

"binhnguyennus/awesome-scalability": ("学习资源", "可扩展性|架构|清单",
  "大规模系统可扩展性、可靠性与性能优化的模式与案例合集。",
  "设计高并发系统时查找业界成熟方案与真实案例。"),

"Eugeny/tabby": ("开发工具", "终端|SSH|跨平台",
  "现代化跨平台终端，内置 SSH/SFTP 会话管理、分屏与插件体系。",
  "需要管理多台服务器连接，又希望终端界面现代好用。"),

"enaqx/awesome-react": ("React", "React|生态|清单",
  "React 生态资源大全，汇总组件库、工具、教程与相关项目。",
  "React 开发中寻找特定功能的成熟库或学习资料。"),

"pallets/flask": ("Python", "Web框架|轻量|微框架",
  "Python 轻量级 Web 框架，核心小而可扩展，路由与模板开箱可用。",
  "写小型服务、内部工具 API，或需要完全自主选型的项目。"),

"openbq-org/OpenBB": ("Python", "金融数据|量化|分析平台",
  "面向分析师、量化研究员与 AI Agent 的开放金融数据平台，统一接入多源行情与基本面数据。",
  "做投研分析、量化策略数据准备与金融 AI 应用。"),

"josephmisiti/awesome-machine-learning": ("学习资源", "机器学习|清单|库推荐",
  "机器学习框架、库与软件的精选清单，按语言与用途分类。",
  "做 ML 项目选型时快速对比不同语言生态下的可用工具。"),

"thedaviddias/Front-End-Checklist": ("学习资源", "前端|检查清单|上线",
  "现代 Web 开发的上线检查清单，覆盖性能、SEO、可访问性与安全等维度。",
  "项目上线前做一轮系统性自查，避免遗漏关键项。"),

"danielmiessler/SecLists": ("安全", "安全字典|渗透测试|Payload",
  "安全测试者必备的字典合集：用户名、密码、目录、Payload 等多种列表。",
  "授权渗透测试、漏洞扫描与安全培训中的字典准备。"),

"fffaraz/awesome-cpp": ("C / C++", "C++|库推荐|清单",
  "C/C++ 框架、库与资源的精选清单，按领域系统分类。",
  "C++ 项目选型，或想了解某个方向有哪些成熟库。"),

"juliangarnier/anime": ("前端其他", "动画库|JavaScript|轻量",
  "轻量级 JavaScript 动画引擎，支持 CSS、SVG、DOM 与对象的复杂时间轴动画。",
  "需要精细控制动画时间轴与缓动曲线的前端项目。"),

"toeverything/AFFiNE": ("前端其他", "知识库|文档协作|白板",
  "下一代知识库工具，把文档、白板与表格融合在同一画布，定位 Notion + Miro。",
  "团队想要既能写文档又能画图的一体化协作空间。"),

"twitter/the-algorithm": ("其他", "推荐算法|Scala|社交",
  "X（Twitter）推荐算法的开源实现，展示大规模社交内容分发的工程结构。",
  "研究推荐系统架构，或学习工业级 Scala 服务组织方式。"),

"unionlabs/union": ("Rust", "跨链|零知识证明|区块链",
  "极简信任假设的零知识跨链桥协议，专注抗审查与高安全性。",
  "研究跨链互操作协议，或搭建 zk 跨链基础设施。"),

"CompVis/stable-diffusion": ("AI / 大模型", "文生图|扩散模型|研究",
  "潜在的文本到图像扩散模型原始实现，是当代 AI 绘画生态的起点。",
  "研究扩散模型原理，或在本地跑原始推理脚本。"),

"calesthio/OpenMontage": ("AI / 大模型", "视频制作|Agent|流水线",
  "面向 Agent 的开源视频生产系统，内置多条制作流水线与大量工具与技能。",
  "想把视频制作流程整体交给 Agent 自动完成。"),

"vuejs/awesome-vue": ("Vue", "Vue|生态|清单",
  "Vue 生态资源精选清单，涵盖组件、插件、工具、教程与项目案例。",
  "Vue 开发中寻找现成组件、插件或学习资源。"),

"Fission-AI/OpenSpec": ("AI / 大模型", "规格驱动|SDD|AI协作",
  "面向 AI 编码助手的规格驱动开发（SDD）工具，先定规格再让 AI 实现。",
  "团队引入 AI 编码后，想用规格约束需求与实现的一致性。"),

"strapi/strapi": ("Node.js / TS", "Headless CMS|内容管理|API",
  "领先的开源 Headless CMS，纯 JS/TS 实现，可视化建模内容类型并自动生成 API。",
  "做内容驱动型产品，需要灵活的内容模型与多端 API。"),

"tw93/Mole": ("开发工具", "清理工具|macOS|CLI",
  "跨平台系统清理与瘦身工具，提供 CLI 与原生应用，清理缓存与冗余文件。",
  "Mac 或 Windows 空间不足，想快速安全地清理系统垃圾。"),

"usestrix/strix": ("安全", "AI渗透测试|漏洞扫描|Agent",
  "开源 AI 渗透测试工具，自动发现并协助修复应用漏洞。",
  "开发阶段做自动化安全扫描，或做授权范围内的渗透测试。"),

"nektos/act": ("DevOps / 云原生", "GitHub Actions|本地运行|CI",
  "在本地用 Docker 运行 GitHub Actions 工作流，省去反复推送调试。",
  "调试 CI 配置时不想每次都提交代码等云端跑。"),

"hakimel/reveal.js": ("前端其他", "演示文稿|HTML|幻灯片",
  "用 HTML 写演示文稿的框架，支持 Markdown、演讲者视图与多种过渡效果。",
  "技术分享想做可版本化、可定制的网页幻灯片。"),

"prakhar1989/awesome-courses": ("学习资源", "公开课|计算机科学|清单",
  "精选的大学计算机课程清单，附课程主页与资料链接。",
  "想按名校课程体系自学计算机核心课程。"),

"moby/moby": ("DevOps / 云原生", "Docker|容器|Go",
  "Moby 项目，容器生态的协作基础，Docker 引擎的上游实现。",
  "研究容器运行时实现，或做容器平台的深度定制。"),

"protocolbuffers/protobuf": ("C / C++", "序列化|RPC|IDL",
  "Google 的跨语言数据交换格式与代码生成工具，高效紧凑，是 gRPC 的基础。",
  "微服务间通信、跨语言数据传输与接口契约定义。"),

"binary-husky/gpt_academic": ("AI / 大模型", "学术写作|论文润色|中文",
  "为大模型优化的学术交互界面，强化论文阅读、润色、翻译与写作体验，支持插件扩展。",
  "科研人员读论文、改稿、做文献总结，上手成本低。"),

"daytonaio/daytona": ("AI / 大模型", "代码沙箱|安全执行|基础设施",
  "安全且弹性的基础设施，用于运行 AI 生成的代码，隔离执行环境。",
  "Agent 需要执行不可信代码时，提供安全隔离沙箱。"),

"hugohe3/ppt-master": ("AI / 大模型", "PPT生成|原生格式|Agent",
  "AI 把文档或主题转成真正的原生 PowerPoint，保留可编辑形状、转场与动画。",
  "需要批量产出可继续编辑的 PPT，而不是图片式幻灯片。"),

"ansible/ansible": ("DevOps / 云原生", "自动化运维|配置管理|无Agent",
  "无 Agent 的 IT 自动化平台，用 YAML 描述服务器配置与应用部署。",
  "批量管理服务器、做配置标准化与自动化发布。"),

"FoundationAgents/MetaGPT": ("AI / 大模型", "多Agent|软件公司|自然语言编程",
  "多 Agent 框架，用角色分工模拟一家 AI 软件公司，从需求直接产出代码。",
  "研究多 Agent 协作，或做「一句话生成软件」的探索。"),

"cline/cline": ("AI / 大模型", "编码Agent|IDE插件|SDK",
  "自主编码 Agent，提供 IDE 扩展、CLI 与 SDK 三种形态，可在编辑器内直接改代码。",
  "在 VS Code 里用 AI 完成跨文件重构与功能开发。"),

"swiftlang/swift": ("移动端", "Swift|iOS|编程语言",
  "Apple 的 Swift 语言官方源码，用于 iOS/macOS 开发，兼顾性能与安全性。",
  "iOS 开发、服务端 Swift，或研究现代编译器与语言设计。"),

"code-yeongyu/oh-my-openagent": ("AI / 大模型", "Agent编排|图工程|工作流",
  "以「图工程」思路编排 Agent 的框架，通过关键词触发复杂任务图。",
  "想把多步骤 Agent 流程组织成可复用、可调试的图结构。"),

"asgeirtj/system_prompts_leaks": ("AI / 大模型", "系统提示词|研究|逆向",
  "收录各家 AI 产品被公开的系统提示词，便于对比其行为约束设计。",
  "研究提示词工程与产品行为边界的设计思路。"),

"microsoft/AI-For-Beginners": ("学习资源", "人工智能|课程|入门",
  "微软的 12 周 AI 入门课，24 节课覆盖搜索、神经网络、CV 与 NLP 基础。",
  "零基础想建立 AI 全貌认知，且希望有配套代码与练习。"),

"dani-garcia/vaultwarden": ("Rust", "密码管理|自托管|Bitwarden",
  "与 Bitwarden 客户端兼容的轻量自托管密码服务器，用 Rust 实现，资源占用低。",
  "想自己托管密码库，又不想跑一整套重型服务。"),

"docling-project/docling": ("AI / 大模型", "文档解析|多格式|结构化",
  "把 PDF、DOCX、PPTX 等文档解析成结构化数据，为生成式 AI 准备干净输入。",
  "构建 RAG 知识库时的文档预处理环节。"),

"BurntSushi/ripgrep": ("Rust", "代码搜索|命令行|正则",
  "极快的递归正则搜索工具，默认尊重 .gitignore，是 grep 的现代替代品。",
  "在大型代码库里秒级搜索关键字与正则模式。"),

"expressjs/express": ("Node.js / TS", "Node框架|极简|中间件",
  "Node.js 最经典的极简 Web 框架，中间件模型灵活，生态庞大。",
  "快速搭 REST API、轻量服务与原型后端。"),

"remotion-dev/remotion": ("React", "视频生成|React|程序化",
  "用 React 组件编写视频，把前端能力用于程序化生成与批量渲染视频。",
  "做数据驱动的动态视频、模板化批量出片。"),

"NanmiCoder/MediaCrawler": ("Python", "爬虫|社交媒体|数据采集",
  "多平台自媒体内容采集工具，支持小红书、抖音、B 站、微博等平台的公开内容抓取。",
  "做舆情分析、内容研究等合规范围内的数据采集。"),

"gorhill/uBlock": ("前端其他", "广告拦截|浏览器扩展|隐私",
  "高效的浏览器内容拦截扩展，拦截广告、跟踪脚本与恶意域名，资源占用低。",
  "想要干净的上网体验并减少隐私追踪。"),
}
