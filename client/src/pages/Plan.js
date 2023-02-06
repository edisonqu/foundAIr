import { useState } from 'react'
import TypeForm from "../components/Typeform";
import NameField from '../components/Form0'
import IdeaField from "../components/Form";
import BudgetField from "../components/Form2";
import CompanyField from "../components/Form3";
import Typewriter from 'typewriter-effect'
import { useNavigate } from 'react-router-dom'
import Backdrop from '@material-ui/core/Backdrop';
import CircularProgress from '@material-ui/core/CircularProgress';
import { makeStyles } from '@material-ui/core/styles';
import { mergeClasses } from '@material-ui/styles';
import Button from "@material-ui/core/Button";
import ButtonGroup from "@material-ui/core/ButtonGroup";
import { motion } from 'framer-motion'

import "./page-styles/Plan.css"


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
  const url = 
"https://cors-anywhere.herokuapp.com/http://www.pdf995.com/samples/pdf.pdf"
// const CID1 = "bafkreicbb5uo4olhe4eptcws4ai2embnqxypcxcsn73j7puhpru75v373q"
  const [name, setName] = useState("");
  const [idea, setIdea] = useState("");
  const [budget, setBudget] = useState("");
  const [company, setCompany] = useState("");
  const [hasData, setHasData] = useState(false);
  const [hasPdf, setHasPdf] = useState(true);
  const [CID, setCID] = useState("")


	const [numPages, setNumPages] = useState(null);
	const [pageNumber, setPageNumber] = useState(1);

  const navigate = useNavigate()

	const onDocumentLoadSuccess = ({ numPages }) => {
		setNumPages(numPages);
	};

	const goToPrevPage = () =>
		setPageNumber(pageNumber - 1 <= 1 ? 1 : pageNumber - 1);

	const goToNextPage = () =>
		setPageNumber(
			pageNumber + 1 >= numPages ? numPages : pageNumber + 1,
		);
    

  


  

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
  }

  

  async function handleConfirm() {
    setHasPdf(false);
    console.log(company, name, idea, budget);
    console.log("fetching")


    // fetch(`https://dsazg33plckom3y6c4draofpl40oaout.lambda-url.us-east-2.on.aws/?company_name=few&author=fewfw%20Qu&idea=fewfwf&budget=fewfewf`, {
    await fetch(`https://dsazg33plckom3y6c4draofpl40oaout.lambda-url.us-east-2.on.aws/?company_name=${company}&author=${name}&idea=${idea}&budget=${budget}`)
    .then((response)=>{
    response.text().then((response)=>{
        console.log(response)
        setCID(response);
        console.log(response);
        console.log("Using CID the value is: "+CID)
        window.localStorage.setItem('cid1',response);
        var CID1 = window.localStorage.getItem('cid1')

        window.location.replace(`https://${CID1}.ipfs.nftstorage.link`)
  })


  return null
  })

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
        <motion.div className='text-7xl flex justify-center'>
            <Typewriter
                  options={{
                    strings:[],
                    autoStart: true,
                    loop: true,
                    delay: 100,
                    
                  }}
                  onInit={(typewriter) => {
                    typewriter
                      .typeString("Designing the Title Page")
                      .pauseFor(5000)
                      .deleteAll()
                      .typeString("Making the Table of Contents")
                      .pauseFor(10000)
                      .deleteAll()
                      .typeString("Creating the Executive Summary")
                      .pauseFor(20000)
                      .deleteAll()
                      .typeString("Producing the Business Overview")
                      .pauseFor(20000)
                      .deleteAll()
                      .typeString("Calculating Competiitve Advantage")
                      .pauseFor(20000)
                      .deleteAll()
                      .typeString("Finding Sales and Market Strategy")
                      .pauseFor(20000)
                      .deleteAll()
                      .typeString("Constructing the Timeline")
                      .pauseFor(20000)
                      .deleteAll()
                      .typeString("Analyazing Finance")
                      .pauseFor(20000)
                      .deleteAll()
                      .typeString("Measuring Key Metrics & Risk Reduction")
                      .pauseFor(20000)
                      .deleteAll()
                      .typeString("Summarizing Conclusion")
                      .pauseFor(30000)
                      .deleteAll()
                  }}
                />
              </motion.div>
      
        </div>
      }

    </div>
  )
}

export default Plan