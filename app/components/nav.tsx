import Link from 'next/link'

const navItems = {
  '/': {
    name: 'home',
  },
  '/blog': {
    name: 'my thoughts',
  },
  'https://gallery.hr1z0n.com/': {
    name: 'gallery',
  },
  '/fun':{
    name: 'fun stuff',
  }
}

export function Navbar() {
  return (
    <aside className="-ml-[8px] mb-16 tracking-tight">
      <div className="lg:sticky lg:top-20">
        <nav
          className="flex flex-row items-start justify-center px-0 pb-0 md:overflow-auto scroll-pr-6 relative"
          id="nav"
        >
          <div className="flex flex-wrap justify-center space-x-4 md:space-x-8 pr-2 md:pr-10">
            {Object.entries(navItems).map(([path, { name }]) => {
              return (
                <Link
                  key={path}
                  href={path}
                  className="transition-all text-base md:text-lg hover:text-neutral-800 dark:hover:text-neutral-200 flex align-middle relative py-1 px-2"
                >
                  {name}
                </Link>
              )
            })}
          </div>
        </nav>
      </div>
    </aside>
  )
}