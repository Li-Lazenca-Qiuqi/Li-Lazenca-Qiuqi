import './App.css'

const hallImage = import.meta.env.BASE_URL + 'images/citadel-hall-frame.png'

const sections = [
  {
    id: 'research',
    number: '01',
    title: '研究',
    description: '数值天气预报、气候模拟与高性能计算。',
    detail: '在复杂系统中寻找可理解的线索。',
  },
  {
    id: 'development',
    number: '02',
    title: '开发',
    description: '用代码把想法做成真正可用的工具。',
    detail: 'Python · C++ · Fortran · React · TypeScript · FastAPI · Tauri',
  },
  {
    id: 'gaming',
    number: '03',
    title: '游戏',
    description: '研究和开发之外，我也是一名游戏玩家。',
    detail: '',
  },
] as const

function App() {
  return (
    <>
      <a className="skip-link" href="#main">跳到正文</a>
      <main className="page-shell" id="top" style={{ borderImageSource: `url("${hallImage}")` }}>

        <div className="page-content" id="main">
          <header className="site-header">
            <a className="wordmark" href="#top" aria-label="奶茶鼠，返回顶部">奶茶鼠</a>
            <nav className="site-nav" aria-label="主要导航">
              {sections.map((section) => (
                <a key={section.id} href={'#' + section.id}>{section.title}</a>
              ))}
            </nav>
          </header>

          <section className="introduction" aria-labelledby="page-title">
            <p className="intro-label">个人主页</p>
            <h1 id="page-title">在好奇心里，<br />继续攀行。</h1>
            <p className="intro-copy">研究天气与气候，编写工具，也在游戏里寻找故事。</p>
          </section>

          <div className="profile-sections">
            {sections.map((section) => (
              <section className="profile-section" id={section.id} key={section.id} aria-labelledby={section.id + '-title'}>
                <span className="section-number" aria-hidden="true">{section.number}</span>
                <h2 id={section.id + '-title'}>{section.title}</h2>
                <p>{section.description}</p>
                {section.detail && <p className="section-detail">{section.detail}</p>}
              </section>
            ))}
          </div>

          {import.meta.env.DEV && (
            <section className="height-preview" aria-labelledby="height-preview-title">
              <div className="height-preview-copy">
                <p className="height-preview-label">本地版面预览</p>
                <h2 id="height-preview-title">故事还可以继续向下。</h2>
                <p>这里预留给之后的作品、笔记与更多内容。现在先看看页面加高后，两侧立柱如何一路延伸到底部。</p>
              </div>
              <div className="height-preview-space" aria-hidden="true">
                <span>后续内容区</span>
              </div>
            </section>
          )}

          <footer className="site-footer">
            <span>奶茶鼠</span>
            <a href="#top">返回顶部 <span aria-hidden="true">↑</span></a>
          </footer>
        </div>
      </main>
    </>
  )
}

export default App
