import React from "react";
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

const Form3 = () => {
  const classes = useStyles();
  return (
    <div>
      <form className={classes.root} autoComplete="off">
        <motion.div
          className="col-md-6 offset-md-3"
          initial={{ y: "50vh" }}
          animate={{ y: 0 }}
          transition={{ stiffness: 150 }}
        >
          <TextField id="contact" required={true} fullWidth label="Contact" />
        </motion.div>
    </form>
    </div>
  )
}

export default Form3