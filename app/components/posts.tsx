import Link from 'next/link'
import { formatDate, getBlogPosts } from 'app/blog/utils'

export function BlogPosts() {
  let allBlogs = getBlogPosts()

  return (
    <div>
      <div className="w-full flex flex-col md:flex-row space-x-0 md:space-x-2">
              <p className="text-neutral-900 dark:text-neutral-100 w-full tracking-tight">
                <u>some recent thoughts/learnings</u>:<br />
              </p>
              {/* <p className="text-neutral-900 dark:text-neutral-100 w-[150px] tracking-tight">
                <u>sequence</u>
              </p>
              <p className="text-neutral-600 dark:text-neutral-400 tabular-nums">
                :&nbsp;<u>domain</u>
              </p>
              <br /> */}
      </div>
      {allBlogs
        .sort((a, b) => {
          if (
            new Date(a.metadata.publishedAt) > new Date(b.metadata.publishedAt)
          ) {
            return -1
          }
          return 1
        })
        .map((post) => (
          <Link
            key={post.slug}
            className="flex flex-col space-y-1 mb-4"
            href={`/blog/${post.slug}`}
          >
            <div className="w-full flex flex-col md:flex-row space-x-0 md:space-x-2">
              <p className="text-neutral-900 dark:text-neutral-100 w-1/2 tracking-tight">
                {post.metadata.title}
              </p>
              <p className="text-neutral-600 dark:text-neutral-400 w-full tabular-nums">
                :&nbsp;{post.metadata.domain} 
                {/* {post.metadata.domain},&nbsp; */}
                {/* {formatDate(post.metadata.publishedAt, false)} */}
              </p>
            </div>
          </Link>
        ))}
    </div>
  )
}
