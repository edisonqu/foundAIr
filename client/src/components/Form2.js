import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import { motion } from "framer-motion";

const useStyles = makeStyles((theme) => ({
  root: {
    "& > *": {
      margin: "8rem auto 5rem",
      maxWidth: "60%"
    }
  }
}));

const Form2 = ({ onSubmit }) => {
  const classes = useStyles();
  return (
      <fieldset className={classes.root} autoComplete="off">
        <motion.div
          className="col-md-6 offset-md-3"
          initial={{ y: "50vh" }}
          animate={{ y: 0 }}
          transition={{ stiffness: 150 }}
        >
        <TextField id="budget" fullWidth label="What is Your Budget" name='budget' required onChange={e => onSubmit(e.target.value)}/>
        </motion.div>
    </fieldset>
  )
}

export default Form2