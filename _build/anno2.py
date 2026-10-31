# -*- coding: utf-8 -*-
A = {
"labuladong/fucking-algorithm": ("学习资源", "算法|LeetCode|题解",
  "以「讲清思路」为核心的算法教程，覆盖动态规划、双指针、KMP 等高频考点与框架套路。",
  "刷 LeetCode 时不想只背答案，想真正理解每类题型的解题框架。"),

"excalidraw/excalidraw": ("前端其他", "白板|绘图|协作",
  "开箱即用的在线手绘风白板，支持实时协作、无限画布与导出图片/源文件。",
  "画架构图、流程图、原型草图，或团队一起在线讨论方案。"),

"ggml-org/llama.cpp": ("C / C++", "LLM推理|量化|本地部署",
  "用纯 C/C++ 实现的 LLM 推理引擎，支持多种量化格式，可在 CPU 与各类设备上跑模型。",
  "在无 GPU 或资源受限的机器上本地部署大模型。"),

"openai/codex": ("AI / 大模型", "编码Agent|终端|Rust",
  "OpenAI 的轻量终端编码 Agent，在本地理解代码库并直接执行开发任务。",
  "习惯命令行的开发者，希望在终端内用 AI 完成改码与排查。"),

"krahets/hello-algo": ("学习资源", "数据结构|算法|动画图解",
  "《Hello 算法》开源教程，动画图解 + 一键运行代码，提供十几种语言的实现版本。",
  "数据结构与算法入门，尤其适合看文字容易卡住、需要图示的学习者。"),

"Chalarangelo/30-seconds-of-code": ("学习资源", "代码片段|JavaScript|速查",
  "大量短小精悍的代码片段合集，按主题整理 JavaScript、CSS、HTML 常用写法。",
  "写代码时想快速查一个惯用写法或小工具函数。"),

"kubernetes/kubernetes": ("DevOps / 云原生", "K8s|容器编排|Go",
  "生产级容器编排系统源码，负责容器调度、服务发现、自动扩缩与滚动发布。",
  "构建或运维大规模容器集群，以及学习云原生调度原理。"),

"rustdesk/rustdesk": ("Rust", "远程桌面|自托管|跨平台",
  "开源远程桌面应用，可完全自建中继服务器，作为 TeamViewer 的替代方案。",
  "需要远程控制设备，又不想把画面数据交给第三方厂商。"),

"shadcn-ui/ui": ("React", "组件库|Tailwind|可定制",
  "不是传统 npm 包，而是可复制进项目的组件源码集合，基于 Tailwind 与 Radix 构建。",
  "想完全掌控组件样式与逻辑，避免被组件库的默认设计绑架。"),

"react/react-native": ("移动端", "React Native|跨平台|iOS/Android",
  "用 React 构建原生移动应用的框架，一套代码同时产出 iOS 与 Android 应用。",
  "前端团队想低成本进入移动端，复用现有 React 技能。"),

"VoltAgent/awesome-design-md": ("前端其他", "设计系统|DESIGN.md|AI",
  "收集各大品牌设计系统的 DESIGN.md 分析文件，放进项目即可让 Agent 生成匹配风格的 UI。",
  "想让 AI 生成的界面贴近某个品牌的设计语言。"),

"Hack-with-Github/Awesome-Hacking": ("安全", "渗透测试|安全清单|CTF",
  "面向黑客、渗透测试与安全研究者的 awesome 清单合集，汇总工具、靶场与学习资源。",
  "入门网络安全，或按方向查找对应的工具与练习平台。"),

"electron/electron": ("前端其他", "桌面应用|Chromium|Node.js",
  "用 HTML/CSS/JS 构建跨平台桌面应用的框架，内置 Chromium 与 Node.js 运行时。",
  "前端团队要做桌面客户端，复用 Web 技术栈。"),

"nodejs/node": ("Node.js / TS", "Node.js|运行时|JavaScript",
  "Node.js 官方源码，把 V8 引擎与事件循环带出浏览器，让 JS 能写服务端。",
  "学习运行时实现，或为 Node 生态贡献代码、排查底层问题。"),

"microsoft/generative-ai-for-beginners": ("AI / 大模型", "生成式AI|课程|Azure",
  "微软出品的 21 节生成式 AI 入门课，配套代码与 Notebook，从提示词讲到应用构建。",
  "零基础想系统了解大模型应用开发，按课程循序推进。"),

"rust-lang/rust": ("Rust", "Rust|编程语言|编译器",
  "Rust 语言官方源码，以所有权模型实现内存安全与高性能并存的系统编程语言。",
  "写高性能系统程序、CLI 工具、WASM 模块，或学习现代编译器设计。"),

"browser-use/browser-use": ("AI / 大模型", "浏览器Agent|自动化|Python",
  "让 AI Agent 直接操作浏览器的开源库，能点击、填表、抓取页面完成真实网页任务。",
  "网页自动化、表单填报、以及需要「看页面再操作」的 Agent 场景。"),

"justjavac/free-programming-books-zh_CN": ("学习资源", "中文书籍|免费资源|清单",
  "免费的计算机编程类中文书籍清单，覆盖各语言、框架与工程实践方向。",
  "想找中文免费电子书系统学习某个技术方向。"),

"godotengine/godot": ("C / C++", "游戏引擎|2D/3D|跨平台",
  "完全开源的多平台 2D/3D 游戏引擎，自带编辑器、场景系统与脚本语言。",
  "独立开发者做小游戏，或想避开商业引擎的授权限制。"),

"earendil-works/pi": ("AI / 大模型", "Agent工具包|LLM|CLI",
  "AI Agent 工具包：统一 LLM 接口、Agent 循环、TUI 界面与编码 Agent 命令行。",
  "想快速搭一个自己的终端 Agent，不想从零写循环与工具层。"),

"TauricResearch/TradingAgents": ("AI / 大模型", "量化交易|多Agent|金融",
  "多 Agent 协作的 LLM 金融交易研究框架，模拟分析师、研究员、交易员分工决策。",
  "研究 AI 在量化投研中的应用，或做多角色协作的决策实验。"),

"immich-app/immich": ("开发工具", "相册|自托管|备份",
  "高性能的自托管照片与视频管理方案，可替代 Google Photos，支持手机自动备份。",
  "想自己掌控照片数据，同时保留 AI 搜图与自动备份体验。"),

"jaywcjlove/awesome-mac": ("学习资源", "macOS|软件推荐|清单",
  "精选 macOS 优质软件清单，按用途分类整理，方便检索与对比。",
  "新入手 Mac，或想找某类工具的最佳选择。"),

"mrdoob/three.js": ("前端其他", "3D|WebGL|可视化",
  "最流行的 JavaScript 3D 库，用 WebGL 在浏览器里渲染三维场景与交互。",
  "网页 3D 展示、产品可视化、数字孪生与创意交互页面。"),

"JuliusBrussee/caveman": ("AI / 大模型", "Token优化|提示词|代理",
  "通过「像原始人一样说话」压缩提示词的 Agent 技能与代理，可削减约 65% 的 token 消耗。",
  "长期用编码 Agent、想显著降低 token 成本。"),

"supabase/supabase": ("Node.js / TS", "Postgres|BaaS|认证",
  "基于 Postgres 的开发平台，提供数据库、认证、存储、实时订阅与 Edge Functions。",
  "快速搭有后端的产品，作为 Firebase 的开源替代。"),

"d3/d3": ("数据可视化", "可视化|SVG|图表",
  "数据驱动文档的底层可视化库，用 SVG、Canvas 与 HTML 构建任意自定义图表。",
  "需要高度定制的图表与数据叙事，而不满足于现成图表组件。"),

"tauri-apps/tauri": ("Rust", "桌面应用|Rust|轻量",
  "用 Rust 做后端、Web 前端做界面的桌面应用框架，产物体积远小于 Electron。",
  "想要小体积、低内存占用的跨平台桌面客户端。"),

"addyosmani/agent-skills": ("AI / 大模型", "Agent Skills|工程化",
  "面向 AI 编码 Agent 的生产级工程技能合集，覆盖规范、测试、评审等环节。",
  "让 Agent 的产出符合团队工程标准，而不是「能跑就行」。"),

"microsoft/TypeScript": ("Node.js / TS", "TypeScript|类型系统|编译器",
  "TypeScript 官方源码，为 JavaScript 加上静态类型系统并编译为干净 JS。",
  "大型前端/Node 项目需要类型保障，或研究类型检查器实现。"),

"openai/whisper": ("AI / 大模型", "语音识别|ASR|多语言",
  "OpenAI 的通用语音识别模型，多语言、抗噪，可本地跑，支持转录与翻译。",
  "会议记录转写、字幕生成、语音数据标注。"),

"stablyai/orca": ("AI / 大模型", "Agent IDE|多Agent|桌面",
  "面向「同时调度多个 Agent」的桌面工作台，可并行运行 Claude Code 等编码 Agent。",
  "一个人要同时推进多个 AI 编码任务，需要统一调度界面。"),

"papers-we-love/papers-we-love": ("学习资源", "论文|计算机科学|阅读",
  "计算机社区精选论文清单与读书会资料，覆盖分布式、语言、算法等经典方向。",
  "想读原始论文打基础，但不知道从哪几篇开始。"),

"fatedier/frp": ("Go", "内网穿透|反向代理|端口映射",
  "高性能反向代理工具，把 NAT 或防火墙后的本地服务安全暴露到公网。",
  "本地开发联调、远程访问家里设备或内网服务。"),

"axios/axios": ("Node.js / TS", "HTTP客户端|Promise|请求库",
  "基于 Promise 的 HTTP 客户端，浏览器与 Node 通用，拦截器与取消机制完善。",
  "前端/Node 项目里统一管理请求、错误处理与鉴权。"),

"paperclipai/paperclip": ("AI / 大模型", "Agent管理|协作|治理",
  "用于在工作场景中管理多个 AI Agent 的开源应用，支持编排、权限与产出治理。",
  "团队要把 Agent 纳入日常工作流，并统一管理其行为边界。"),

"denoland/deno": ("Node.js / TS", "Deno|运行时|TypeScript",
  "现代 JavaScript/TypeScript 运行时，默认安全沙箱、原生 TS 支持、内置工具链。",
  "写脚本与工具时想要更安全的权限模型和免配置体验。"),

"google-gemini/gemini-cli": ("AI / 大模型", "Gemini|终端Agent|MCP",
  "Google 官方开源终端 AI Agent，把 Gemini 能力接入命令行，支持 MCP 工具扩展。",
  "在终端里用 Gemini 完成代码问答、文件操作与自动化任务。"),

"rasbt/LLMs-from-scratch": ("AI / 大模型", "从零实现|LLM|PyTorch",
  "从零用 PyTorch 一步步实现类 ChatGPT 大模型的教程与配套代码。",
  "想真正搞懂 Transformer、注意力与训练流程，而不是只会调 API。"),

"ruanyf/weekly": ("学习资源", "科技周刊|中文|资讯",
  "阮一峰的科技爱好者周刊，每周五更新，汇总工具、文章、资源与行业观察。",
  "想低成本保持技术视野，每周固定读一份精选资讯。"),

"Panniantong/Agent-Reach": ("AI / 大模型", "数据获取|CLI|Agent",
  "给 AI Agent 装上「看互联网」的能力：一个 CLI 读取 Twitter、Reddit、YouTube、B 站等平台内容。",
  "Agent 需要跨平台搜集真实用户内容与舆情时。"),

"thedotmack/claude-mem": ("AI / 大模型", "Agent记忆|上下文|持久化",
  "为 Agent 提供跨会话的持久上下文：记录过程、压缩摘要，再按需注入提示词。",
  "长期使用编码 Agent，希望它记住历史决策与项目约定。"),

"Leonxlnx/taste-skill": ("AI / 大模型", "Agent Skills|设计品味|前端",
  "给编码 Agent 注入「审美」的技能：艺术方向、参考图与浏览器校验，避免生成模板味页面。",
  "受够了 AI 生成的千篇一律前端页面，想要有设计感的产出。"),

"goldbergyoni/nodebestpractices": ("Node.js / TS", "Node.js|最佳实践|工程规范",
  "Node.js 最佳实践清单，覆盖项目结构、错误处理、测试、安全与生产部署。",
  "搭建或重构 Node 服务时，对照检查工程规范是否到位。"),

"microsoft/terminal": ("开发工具", "终端|Windows|命令行",
  "Windows Terminal 与经典控制台宿主源码，支持多标签、GPU 渲染与自定义主题。",
  "Windows 上想要现代化终端体验，或研究终端渲染实现。"),

"nexu-io/open-design": ("AI / 大模型", "AI设计|协作|本地优先",
  "可协作的 AI 设计工作台，本地优先、开源，用于产出动效、原型、页面与演示。",
  "设计中需要用 AI 快速生成可交付的视觉稿与交互原型。"),

"pytorch/pytorch": ("AI / 大模型", "深度学习|GPU|Python",
  "动态图深度学习框架，张量计算与自动求导，科研与工业界的首选之一。",
  "模型研发、实验迭代，以及需要灵活调试网络结构的场景。"),

"deepseek-ai/DeepSeek-V3": ("AI / 大模型", "DeepSeek|MoE|开源模型",
  "DeepSeek 第三代 MoE 大模型的开源仓库，含模型权重、推理代码与技术报告。",
  "自建推理服务、做领域微调，或研究 MoE 架构实现。"),

"fastapi/fastapi": ("Python", "Web框架|异步|OpenAPI",
  "高性能 Python Web 框架，基于类型注解自动生成校验与 OpenAPI 文档。",
  "快速开发 API 服务，尤其是需要异步与自动文档的后端。"),

"Anduin2017/HowToCook": ("其他", "做饭|程序员文化|菜谱",
  "程序员做饭指南，用工程化思维把家常菜拆成可复现的步骤与用量。",
  "刚独立生活、想按步骤做出能吃的家常菜。"),

"neovim/neovim": ("开发工具", "编辑器|Vim|Lua",
  "Vim 的现代化重构版本，内置 LSP、异步插件与 Lua 配置，扩展性强。",
  "习惯纯键盘编辑、想把编辑器打造成专属 IDE。"),

"react/create-react-app": ("React", "脚手架|零配置|React",
  "一条命令创建 React 应用的经典脚手架，零配置起步。",
  "快速验证 React 想法；新项目更推荐 Vite 或 Next.js。"),

"ruvnet/RuView": ("Rust", "WiFi感知|IoT|智能家居",
  "把普通 WiFi 信号转成空间感知能力，实现存在检测与生命体征监测，无需摄像头。",
  "隐私敏感的居家监测、老人看护与智能家居联动。"),

"angular/angular": ("前端其他", "Angular|企业级|TypeScript",
  "Google 的企业级前端框架，内置依赖注入、路由、表单与强类型模板。",
  "大型团队长期维护的中后台系统，需要强约束与完整方案。"),

"mtdvio/every-programmer-should-know": ("学习资源", "计算机通识|清单|基础",
  "一份「每个程序员都该知道」的技术常识合集，覆盖底层原理、工具与工程习惯。",
  "自查知识盲区，或给新人做基础扫盲清单。"),

"ant-design/ant-design": ("React", "组件库|企业级|设计语言",
  "企业级 UI 设计语言与 React 组件库，中后台组件覆盖度极高。",
  "做管理后台、数据平台等重表单重表格的业务系统。"),

"mui/material-ui": ("React", "组件库|Material Design|React",
  "实现 Google Material Design 的 React 组件库，主题系统成熟、组件齐全。",
  "需要一套完整、可定制主题的 React 组件体系。"),

"microsoft/playwright": ("开发工具", "E2E测试|浏览器自动化|跨浏览器",
  "端到端测试与浏览器自动化框架，一套 API 驱动 Chromium、Firefox 与 WebKit。",
  "写稳定的 E2E 测试，或做网页抓取与自动化操作。"),

"karpathy/autoresearch": ("AI / 大模型", "自动研究|Agent|训练",
  "让 AI Agent 在单卡上自动跑研究实验的项目，自动完成训练与结果分析循环。",
  "研究 Agent 驱动的自动化机器学习实验。"),

"florinpop17/app-ideas": ("学习资源", "练手项目|灵感|分级",
  "按难度分级的应用开发练习题目库。",
  "学完语法后不知道做什么项目，需要一份循序渐进的练手清单。"),

"tailwindlabs/tailwindcss": ("前端其他", "CSS框架|原子化|实用类",
  "原子化 CSS 框架，用工具类直接写样式，配合设计令牌实现快速且一致的 UI。",
  "希望样式与组件同文件维护、避免 CSS 命名冲突的项目。"),

"nvbn/thefuck": ("开发工具", "命令行|纠错|效率",
  "自动纠正上一条输错的终端命令，支持 git、docker、apt 等大量命令。",
  "经常敲错命令，想少打一遍或少查一次文档。"),

"pbakaus/impeccable": ("AI / 大模型", "Agent Skills|设计语言|审查",
  "为编码 Agent 提供设计词汇表，用 polish、critique 等指令打磨与审查界面质量。",
  "想系统性地提升 AI 生成界面的完成度与一致性。"),

"punkpeye/awesome-mcp-servers": ("AI / 大模型", "MCP|工具集成|清单",
  "MCP（Model Context Protocol）服务器合集，让 AI 客户端接入各类外部工具与数据源。",
  "给 Claude、Cursor 等客户端寻找现成的 MCP 工具接入。"),

"microsoft/Web-Dev-For-Beginners": ("学习资源", "Web开发|课程|入门",
  "微软的 24 节 Web 开发入门课，12 周从 HTML/CSS 讲到 JS 与部署。",
  "零基础转前端，需要结构化、带练习的入门课程。"),

"OpenCut-app/OpenCut": ("前端其他", "视频编辑|开源|剪映替代",
  "开源的在线视频编辑器，定位为剪映/CapCut 的替代方案，浏览器内完成剪辑。",
  "需要轻量视频剪辑，又不想装重型软件或付费订阅。"),

"localsend/localsend": ("移动端", "局域网传输|跨平台|AirDrop替代",
  "跨平台局域网文件互传工具，手机与电脑同网即可高速传输，替代 AirDrop。",
  "在 Windows、macOS、Android、iOS 之间快速传文件。"),

"oven-sh/bun": ("Node.js / TS", "运行时|打包器|包管理",
  "一体化 JavaScript 工具链：运行时、打包器、测试运行器与包管理器，速度极快。",
  "想用更快的 Node 替代品，或减少前端工具链的启动开销。"),

"NationalSecurityAgency/ghidra": ("安全", "逆向工程|反汇编|软件分析",
  "NSA 开源的软件逆向工程框架，提供反汇编、反编译与脚本化分析能力。",
  "恶意样本分析、漏洞研究、闭源程序逆向。"),

"vllm-project/vllm": ("AI / 大模型", "推理引擎|高吞吐|部署",
  "高吞吐、显存高效的大模型推理与服务引擎，支持 PagedAttention 与连续批处理。",
  "生产环境部署 LLM 服务，追求吞吐与成本的最优解。"),

"3b1b/manim": ("Python", "数学动画|可视化|Python",
  "3Blue1Brown 使用的数学动画引擎，用代码精确生成讲解型数学视频。",
  "制作数学/算法讲解视频，或需要高质量程序化动画。"),

"debpalash/VoiceStudio": ("AI / 大模型", "语音克隆|配音|本地",
  "完全本地运行的开源语音工作室，支持声音克隆、配音、听写与有声书制作。",
  "需要离线处理语音，且不想把声音数据上传云端。"),

"puppeteer/puppeteer": ("Node.js / TS", "浏览器自动化|Chrome|爬虫",
  "通过 DevTools 协议控制 Chrome/Firefox 的 Node 库，用于自动化与页面抓取。",
  "生成 PDF、截图、爬取动态渲染页面与自动化测试。"),

"nvm-sh/nvm": ("开发工具", "Node版本管理|Shell|环境",
  "POSIX 兼容的 Node 版本管理脚本，一条命令切换不同 Node 版本。",
  "同时维护多个项目，需要切换 Node 版本避免依赖冲突。"),

"Stirling-Tools/Stirling-PDF": ("开发工具", "PDF处理|自托管|Docker",
  "功能齐全的自托管 PDF 工具箱：合并、拆分、转换、OCR、签名与水印。",
  "需要批量处理 PDF，又不想把敏感文件上传到在线工具。"),

"sherlock-project/sherlock": ("安全", "开源情报|账号检索|OSINT",
  "通过用户名在数百个社交平台上检索账号是否存在的开源情报工具。",
  "安全审计、品牌保护与授权范围内的公开信息核查。"),

"iluwatar/java-design-patterns": ("Java", "设计模式|Java|教学",
  "用 Java 实现全部经典设计模式的示例仓库，每个模式都有场景说明与代码。",
  "学习设计模式落地写法，或在代码评审中统一设计语言。"),

"odysseus-dev/odysseus": ("AI / 大模型", "自托管|AI工作台|隐私",
  "可自托管的 AI 工作空间，把对话、知识与工具集中在一个私有环境里。",
  "对数据隐私敏感，想在自己的服务器上跑 AI 工作流。"),
}
