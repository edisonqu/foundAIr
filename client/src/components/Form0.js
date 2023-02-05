import { useState } from "react";
import { motion } from "framer-motion";
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";

const useStyles = makeStyles((theme) => ({
  root: {
    "& > *": {
      margin: "8rem auto 5rem",
      maxWidth: "60%"
    }
  }
}));

const Form0 = ({ onSubmit }) => {
const classes = useStyles();
  return (
    <fieldset className={classes.root} autoComplete="off">
    <motion.div
      className="col-md-6 offset-md-3"
      initial={{ y: "50vh" }}
      animate={{ y: 0 }}
      transition={{ stiffness: 150 }}
    >
    <TextField id="name" fullWidth label="What is your Name" name='name' required onChange={e => onSubmit(e.target.value)}/>
    </motion.div>
</fieldset>
  )
}

export default Form0