// import React from 'react';  // Imported by next.js 

import Link from 'next/link';

const Home = props => (
	<div>
		<p>Hey!</p>
		<Link href="/sell">
			<a>Sell</a>
		</Link>
	</div>
)  // Functional Stateless Component

export default Home;