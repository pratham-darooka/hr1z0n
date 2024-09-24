import { BlogPosts } from 'app/components/posts'
import Link from 'next/link'

export const metadata = {
  title: 'my thoughts',
  description: 'Read hr1z0n\'s thoughts and experiences.',
}

export default function Page() {
  return (
    <section>
      <h1 className="font-semibold text-2xl mb-8 tracking-tighter">
        🧠 welcome to my brain
      </h1>
      <BlogPosts />
      <br />
      <Link href="https://github.com/pratham-darooka/hr1z0n/discussions">
        discuss your thoughts with the community <u>here</u>!
      </Link>
      <br />
      <br />
      <Link href="/blog/chat">
        chat with me <u>here</u>! (feature under development)
      </Link>
    </section>
  )
}
