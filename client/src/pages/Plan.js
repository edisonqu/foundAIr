import { useState } from 'react'
import TypeForm from "../components/Typeform";
import NameField from '../components/Form0'
import IdeaField from "../components/Form";
import BudgetField from "../components/Form2";
import CompanyField from "../components/Form3";
import Typewriter from 'typewriter-effect'

import Backdrop from '@material-ui/core/Backdrop';
import CircularProgress from '@material-ui/core/CircularProgress';
import { makeStyles } from '@material-ui/core/styles';
import { mergeClasses } from '@material-ui/styles';

import Button from "@material-ui/core/Button";
import ButtonGroup from "@material-ui/core/ButtonGroup";

const useStyles = makeStyles((theme) => ({
  backdrop: {
    zIndex: theme.zIndex.drawer + 1,
    color: '#fff',
  },
}));

const Plan = () => {
  
  const classes = useStyles();
  let data = false;
  let pdf = true;
  const [name, setName] = useState("");
  const [idea, setIdea] = useState("");
  const [budget, setBudget] = useState("");
  const [company, setCompany] = useState("");
  const [hasData, setHasData] = useState(false);
  const [hasPdf, setHasPdf] = useState(true);
  

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
    console.log(name, idea, budget, company)
    data = {name, idea, budget, company};
    setHasData(true);
    console.log(data);
    console.log("asdsda");

  }

  const handleConfirm = () => {
    setHasPdf(false);
    fetch(`https://dsazg33plckom3y6c4draofpl40oaout.lambda-url.us-east-2.on.aws/?company_name=${company}&author=${name} Qu&idea=${idea}&budget=${budget}`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json',
     },
  })
  console.log("fetched data!")
  }
    
  return (
    <div className="h-screen bg-white">
      <h1 className='text-center text-6xl mt-16 font-bold'>Generate Plan</h1>

      <TypeForm onSubmit={handleSubmit}>
        <NameField onSubmit={chooseName} />
        <IdeaField onSubmit={chooseIdea}/>
        <BudgetField onSubmit={chooseBudget} />
        <CompanyField onSubmit={chooseCompany}/>
      </TypeForm>
      {hasData && 
        <div className='mt-16 items-center justify-center pb-24 px-32 rounded-2xl'>
          <h1 className='text-5xl font-bold'>Confirm Your Business Info</h1>
          <div className='text-4xl mt-6'>
            <h1 className='my-2'><span className='font-bold'>Name: </span> {name}</h1>
            <h1 className='my-2'><span className='font-bold'>Company Name: </span> {company}</h1>
            <h1 className='my-2'><span className='font-bold'>Ideas: </span> {idea}</h1>
            <h1 className='mt-2 mb-6'><span className='font-bold'>Budget: </span>{budget}</h1>
            <ButtonGroup
            disableElevation
            size="large"
            variant="contained"
            color="primary"
            >
              <Button className='' onClick={handleConfirm}>Confirm</Button>
            </ButtonGroup>
          </div>

        </div>
      }

      {hasPdf ? hasPdf : 
      <div className='flex flex-col'>
        <Backdrop className={classes.backdrop} open>
          <CircularProgress color="inherit" />
        </Backdrop>
      
        </div>
      }

    </div>
  )
}

export default Plan