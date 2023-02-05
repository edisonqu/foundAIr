import React from 'react'
import BlockRevealAnimation from 'react-block-reveal-animation';

import "./page-styles/Home.css"
import ImageOne from '../components/imageOne.js'
import imageTwo from '../components/imageTwo.js'
import imageThree from '../components/imageThree.js'
import ImageFour from '../components/ImageFour.js'
import TextBox from  '../components/TextBox'

const Home = () => {
  return (
    <div>
      <BlockRevealAnimation>
        This will be revealed
      </BlockRevealAnimation>
    </div>
  );
  }
export default Home;