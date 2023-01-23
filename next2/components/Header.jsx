import React from "react";
import Link from "next/link";
const Header = () => {
  return (
    <header>
      <ul>
        <li>
          <Link href="/">
          home
          </Link>
        </li>
      </ul>
      <ul>
        <li>
          <Link href="/posts/[id]" as="/posts/first">
            First Post
          </Link>
        </li>
      </ul>
      <ul>
        <li>
          <Link href="/posts/[id]" as="/posts/second">
            Second Post
          </Link>
        </li>
      </ul>
    </header>
  );
};

export default Header;