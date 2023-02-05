import { useState } from 'react'
import TypeForm from "../components/Typeform";
import NameField from '../components/Form0'
import IdeaField from "../components/Form";
import BudgetField from "../components/Form2";
import CompanyField from "../components/Form3";
import Typewriter from 'typewriter-effect'

import Backdrop from '@material-ui/core/Backdrop';
import CircularProgress from '@material-ui/core/CircularProgress';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';
import { mergeClasses } from '@material-ui/styles';

const useStyles = makeStyles((theme) => ({
  backdrop: {
    zIndex: theme.zIndex.drawer + 1,
    color: '#fff',
  },
}));

const Plan = () => {
  
  const classes = useStyles();
  const pdf = false;
  const [name, setName] = useState("");
  const [idea, setIdea] = useState("");
  const [budget, setBudget] = useState("");
  const [company, setCompany] = useState("");

  const chooseName = (value) => {
    setName(value);
  }
  const chooseIdea = (value) => {
    setIdea(value);
    console.log(idea);
  }
  const chooseBudget = (value) => {
    setBudget(value);
  }
  const chooseCompany = (value) => {
    setCompany(value);
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(name, idea, budget, company)
    const data = {name, idea, budget, company};

    fetch('', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
  })
  }

  return (
    <div className="h-screen bg-white">
      <h1 className='text-center text-6xl'>Generate Plan</h1>
      <TypeForm onSubmit={handleSubmit}>
        <NameField onSubmit={chooseName} />
        <IdeaField onSubmit={chooseIdea}/>
        <BudgetField onSubmit={chooseBudget} />
        <CompanyField onSubmit={chooseCompany}/>
      </TypeForm>
      {pdf ? pdf : 
      <div>
        <Backdrop className={classes.backdrop} open>
          <CircularProgress color="inherit" />
        </Backdrop>
        <div className='text-3xl mt-48 flex justify-center'>
          <Typewriter
                options={{
                  strings:[],
                  autoStart: true,
                  loop: true,
                  delay: 100,
                }}
                onInit={(typewriter) => {
                  typewriter
                    .pauseFor(1000)
                    .typeString("Loading1")
                    .pauseFor(1000)
                    .deleteAll()
                    .typeString("Loading2")
                    .pauseFor(1000)
                    .deleteAll()
                    .typeString("Loading3")
                    .pauseFor(1000)
                    .deleteAll()
                    .typeString("Loading4")
                }}
              />
            </div>
        </div>
      }

    </div>
  )
}

export default Plan