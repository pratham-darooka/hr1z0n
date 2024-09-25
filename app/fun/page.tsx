import Link from 'next/link'

export const metadata = {
  title: 'fun',
  description: 'Have fun with hr1z0n\'s developments.',
}

const Page = () => {
  return (
    <div>
        <h1 className="font-semibold text-2xl mb-8 tracking-tighter">
          🎮 have some fun here
        </h1>
          <Link href='https://pictionary-ai.vercel.app/'>
            : play pictionary with ai, compete and get on top of the leaderboard<br />(under development)
          </Link>
          <br />
          <br />
          <Link href='https://pictionary-ai-freeplay.vercel.app/'>
            : freeplay pictionary with ai
          </Link>
          <br />
          <br />
          <Link href='https://promptify-text.vercel.app/'>
            : convert your text into something beautiful
          </Link>
    </div>
  );
};

export default Page;