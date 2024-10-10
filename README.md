# TikTokDownloader
⚠️  仅供参考，源码在github上。
<p>🔥 <b>TikTok 主页/合辑/直播/视频/图集/原声；抖音主页/视频/图集/收藏/直播/原声/合集/热榜数据采集工具：</b>完全开源，基于 HTTPX 模块实现的免费工具；批量下载抖音账号发布、喜欢、收藏作品；批量下载 TikTok 账号发布、喜欢作品；下载抖音链接或 TikTok 链接作品；获取抖音直播推流地址；下载抖音直播视频；获取 TikTok 直播推流地址；下载 TikTok 直播视频；批量下载抖音合集作品；批量下载 TikTok 合辑作品；采集抖音热榜数据。</p>
<p>⭐ 本项目完全免费开源，无任何收费功能，请勿上当受骗！</p>
<hr>

# 📝 项目功能\(Function\)

* ✅ 下载抖音无水印视频/图集
* ✅ 下载 TikTok 无水印视频/图集
* ✅ 批量下载抖音账号发布/喜欢/收藏作品
* ✅ 批量下载 TikTok 账号发布/喜欢作品
* ✅ 采集抖音 / TikTok 详细数据
* ✅ 批量下载链接作品
* ✅ 多账号批量下载作品
* ✅ 自动跳过已下载的文件
* ✅ 持久化保存采集数据
* ✅ 下载动态/静态封面图
* ✅ 获取抖音直播推流地址
* ✅ 获取 TikTok 直播推流地址
* ✅ 调用 ffmpeg 下载直播
* ✅ Web UI 交互界面
* ✅ 采集抖音作品评论数据
* ✅ 批量下载抖音合集作品
* ✅ 批量下载 TikTok 合辑作品
* ✅ 记录点赞收藏等统计数据
* ✅ 筛选作品发布时间
* ✅ 支持账号作品增量下载
* ✅ 支持使用代理采集数据
* ✅ 支持局域网远程访问
* ✅ 采集抖音账号详细数据
* ✅ 作品统计数据更新
* ✅ 自动更新账号昵称
* ✅ 部署至私有服务器
* ✅ 部署至公开服务器
* ✅ 采集抖音搜索数据
* ✅ 采集抖音热榜数据
* ✅ 记录已下载作品 ID
* ☑️ 扫码登陆获取 Cookie
* ✅ 从浏览器获取 Cookie
* ✅ 支持 Web API 调用
* ✅ 支持多线程下载作品
* ✅ 文件完整性处理机制
* ✅ 自定义规则筛选作品
* ✅ 支持文件断点续传下载


# 📋 项目说明\(Instructions\)

## 快速入门

<p>⭐ Mac OS、Windows 10 及以上用户可前往 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 下载已编译的程序，开箱即用！</p>
<p><strong>注意：Mac OS 平台可执行文件 <code>main</code> 可能需要从终端命令行启动；受设备限制，Mac OS 平台可执行文件尚未经过测试，无法保证可用性！</strong></p>
<hr>
一、运行方式
<ol>
<li><b>运行可执行文件</b>
<ol>
<li>下载 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 发布的可执行文件压缩包</li>
<li>解压后打开程序文件夹，双击运行 <code>main</code></li>
</ol>
</li>
<li><b>配置环境运行</b>
<ol>
<li>安装不低于 <code>3.12</code> 版本的 <a href="https://www.python.org/">Python</a> 解释器</li>
<li>下载 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 发布的源码至本地</li>
<li>运行 <code>pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt</code> 命令安装程序所需模块</li>
<li>运行 <code>python main.py</code> 命令启动 TikTokDownloader</li>
</ol>
</li> 
</ol>

二、阅读免责声明，根据提示输入内容

三、将 Cookie 信息写入配置文件
<ol>
<li><b>手动粘贴 Cookie（推荐）</b>
<ol>
<li>参考 <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md">Cookie 提取教程</a>，复制所需 Cookie</li>
<li>选择 <code>复制粘贴写入 Cookie</code> 选项，按照提示将 Cookie 写入配置文件</li>
</ol>
<li><b>从浏览器获取 Cookie（推荐）</b>
<ol>选择 <code>从浏览器获取 Cookie</code> 选项，按照提示选择浏览器类型
</ol>
<li><b>扫码登录获取 Cookie（弃用）</b>
<ol>
<li>选择 <code>扫码登录获取 Cookie</code> 选项，程序会显示登录二维码图片，并使用默认应用打开图片</li>
<li>使用抖音 APP 扫描二维码并登录账号</li>
<li>按照提示操作，将 Cookie 写入配置文件</li>
</ol>
</li>
</ol>
四、返回程序界面，依次选择 <code>终端交互模式</code> -> <code>批量下载链接作品(通用)</code> -> <code>手动输入待采集的作品链接</code>

五、输入抖音作品链接即可下载作品文件
<hr>

# ⚠️ 免责声明\(Disclaimers\)

<ul>
<li>使用者对本项目的使用由使用者自行决定，并自行承担风险。作者对使用者使用本项目所产生的任何损失、责任、或风险概不负责。</li>
<li>本项目的作者提供的代码和功能是基于现有知识和技术的开发成果。作者尽力确保代码的正确性和安全性，但不保证代码完全没有错误或缺陷。</li>
<li>使用者在使用本项目时必须严格遵守 <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/license">GNU
    General Public License v3.0</a> 的要求，并在适当的地方注明使用了 <a
        href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/license">GNU General Public License
    v3.0</a> 的代码。
</li>
<li>使用者在任何情况下均不得将本项目的作者、贡献者或其他相关方与使用者的使用行为联系起来，或要求其对使用者使用本项目所产生的任何损失或损害负责。</li>
<li>使用者在使用本项目的代码和功能时，必须自行研究相关法律法规，并确保其使用行为合法合规。任何因违反法律法规而导致的法律责任和风险，均由使用者自行承担。</li>
<li>本项目的作者不会提供 TikTokDownloader 项目的付费版本，也不会提供与 TikTokDownloader 项目相关的任何商业服务。</li>
<li>基于本项目进行的任何二次开发、修改或编译的程序与原创作者无关，原创作者不承担与二次开发行为或其结果相关的任何责任，使用者应自行对因二次开发可能带来的各种情况负全部责任。</li>
</ul>
<b>在使用本项目的代码和功能之前，请您认真考虑并接受以上免责声明。如果您对上述声明有任何疑问或不同意，请不要使用本项目的代码和功能。如果您使用了本项目的代码和功能，则视为您已完全理解并接受上述免责声明，并自愿承担使用本项目的一切风险和后果。</b>
