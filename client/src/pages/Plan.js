import React from 'react'
import TypeForm from "../components/Typeform";
import BasicTextFields from "../components/Form";
import EmailField from "../components/Form2";
import ContactField from "../components/Form3";

const Plan = () => {
  const submit = (data) => {
    return console.log(data);
  };
  return (
    <div>
      <h1>asdasdasdasd</h1>
      <TypeForm onSubmit={submit}>
        <BasicTextFields />
        <EmailField />
        <ContactField />
      </TypeForm>
    </div>
  )
}

export default Plan