import React from 'react'
import BlockRevealAnimation from 'react-block-reveal-animation';
import { Link } from "react-router-dom"
import Typewriter from 'typewriter-effect'
import "./page-styles/Home.css"
import TextBox from  '../components/TextBox'
import { motion } from 'framer-motion'
import Mac from '../images/Scroll.png'

const Home = () => {
  const container = {
    hidden: {
      opacity: 0,
    },
    visible: {
      y: 0,
      opacity: 1,
      transition: {
        staggerChildren: 0.5,
        
      },
    },
    exit: {
        y: '-10vh',
        opacity: 0,
        transition: {
          duration: 0.25,
        }
    },
  };

  const textUp = {
    hidden: {
        y: '5vh',
        opacity: 0,
    },
    visible: { 
        y: 0,
        opacity: 1,
        transition: {
            duration: 1.5,
            ease: [0.6, 0.01, 0.05, 0.95],
        }
    },
    exit: {
        opacity: 0,
    },
  };

  const textSide = {
    hidden: {
        x: '-5vh',
        opacity: 1,
    },
    visible: { 
        x: 0,
        opacity: 1,
        transition: {
            duration: 2,
            ease: [0.6, 0.01, 0.05, 0.95],
        }
    },
    exit: {
        opacity: 0,
    },
  };

  const textLeft = {
    hidden: {
        x: '-5vh',
        opacity: 0,
    },
    visible: { 
        x: 0,
        opacity: 1,
        transition: {
            duration: 1.5,
            ease: [0.6, 0.01, 0.05, 0.95],
        }
    },
    exit: {
        opacity: 0,
    },
  };
  return (
    <motion.div className='h-screen bg-no-repeat object-cover content-center'
    variants={container}
    initial='hidden'
    animate='visible'
    exit='exit'>
      <div className='flex justify-evenly items-center h-screen'>
        <div className='flex flex-col'>
          <motion.h1 variants={textUp} className='text-8xl text-black mt-48 font-bold'>Have an Idea?</motion.h1>
          <motion.h1 variants={textUp} className='text-7xl text-black mt-8 font-bold'>Found<span className='text-red-800 font-bold'>AI</span>r has a Plan</motion.h1>
          <motion.h1 variants={textUp} className='text-5xl text-black mt-10'>Become a Found<span className='text-red-800 font-bold'>AI</span>r faster than Ev<span className='text-red-800 font-bold'>AI</span>r</motion.h1>
          <motion.h1 variants={textUp} className='text-5xl text-black mt-10'>Using <span className='text-red-800 font-bold'>AI</span> generated business plans.</motion.h1>
          <Link to='/plan'>
            <motion.button 
              whileHover={{scale:1.1}}
              whileTap={{scale:0.9}}
              variants={textUp}
              className='bg-red-700 text-white hover:bg-red-900 hover:text-white font-bold text-6xl text-center border-2 border-solid border-red-900 px-12 mt-32 py-4 rounded-2xl duration-300 transition-colors text-2xl" data-test-id={`navbar-logout`}'>Get Started
            </motion.button>
          </Link>
        </div>
        <div>
          <motion.img variants={textLeft} className='certificate mt-36 scroll' src={Mac} />
        </div>
      </div>
    </motion.div>
  );
  }
export default Home;