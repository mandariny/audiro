import Link from 'next/link';

export default function FirstPost() {
    return (
    <>
    
      <button><a href={'https://www.naver.com'}>네이버 </a> </button>
      <br/>
      <button><a href={'https://www.kakao.com'}>카카오 </a> </button>
      <br/>
      <button><a href={'https://www.google.com'}>구글 </a> </button>
      <br/>

    <Link href="/">Back to home</Link>
    </>
    )
  }