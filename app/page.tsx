import { BlogPosts } from 'app/components/posts'

export default function Page() {
  return (
    <section>
      <h1 className="mb-8 text-2xl font-semibold tracking-tighter">
        👾 hi, i'm hr1z0n :]
      </h1>
      <p className="mb-4">
        {/* If you find this: Here's the original that was rephrased by AI :] */}
        {/* {`I'm a gen z trying to make a living off my passion for generative ai.
        I am super interested in finance, particulary the stock market and personal finance.
        I was born and brought up in India, and have also lived in the US for a litle over 5 years.
        I don't really like to talk much about myself and create social media content
        but I am creating this website to share my thoughts and experiences with the world.
        I am a unsocial person and usually pretty lonely. I hope this site helps you find your way.
        Will keep adding more content as I learn more about myself and my journey.
        These blogs would be for my knowledge but will be rephrased using AI - I am not a good writer.`} */}
        
        {`i am an avid enthusiast of generative AI (something I used to rephrase this bio and make my thoughts less snarky), 
        wholeheartedly pursuing my passion as a career.
        financial stuff, particularly the stock market sparks my curiosity, 
        and i also gravitate towards personal finance development, 
        eagerly diving into the nuances.`}
        <br/>
        <br/>
        {`born and raised in india, i later resided in the usa for over 5 years,  
        cultivating a diverse worldview and unique perspectives.`}
        <br/>
        <br/>
        <u>disclaimer</u>
        {`: blogs have my opinions and experiences, and i am not a professional anything.
        i am just a human being, and i hope this site helps you find your way.`}
      </p>
      <div className="my-8">
        <BlogPosts />
      </div>
    </section>
  )
}
