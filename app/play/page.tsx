import Head from 'next/head';
import Link from 'next/link'

const Page = () => {
  return (
    <div>
        <h1 className="font-semibold text-2xl mb-8 tracking-tighter">
          have some fun here 🎮
        </h1>
          <Link href='https://pictionary-ai.vercel.app/'>
            : play pictionary with ai (feature under development)
          </Link>
    </div>
  );
};

export default Page;