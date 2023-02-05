import { useState } from 'react'
import TypeForm from "../components/Typeform";
import IdeaField from "../components/Form";
import BudgetField from "../components/Form2";
import CompanyField from "../components/Form3";

const Plan = () => {
  const [idea, setIdea] = useState("");
  const [budget, setBudget] = useState("");
  const [company, setCompany] = useState("");

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

  const handleSubmit = () => {
    console.log(idea, budget, company)
  }

  


  return (
    <div className="h-screen bg-white">
      <h1 className='text-center text-6xl'>Generate Plan</h1>
      <TypeForm onSubmit={handleSubmit}>
        <IdeaField onSubmit={chooseIdea}/>
        <BudgetField onSubmit={chooseBudget} />
        <CompanyField onSubmit={chooseCompany}/>
      </TypeForm>
    </div>
  )
}

export default Plan