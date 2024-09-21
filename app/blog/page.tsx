import { BlogPosts } from 'app/components/posts'

export const metadata = {
  title: 'my thoughts',
  description: 'Read my thoughts and experiences.',
}

export default function Page() {
  return (
    <section>
      <h1 className="font-semibold text-2xl mb-8 tracking-tighter">welcome to my brain</h1>
      <BlogPosts />
    </section>
  )
}
