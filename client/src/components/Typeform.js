import React, { useState } from "react";
import Button from "@material-ui/core/Button";
import ButtonGroup from "@material-ui/core/ButtonGroup";
import { makeStyles } from "@material-ui/core/styles";
import Confirm from "./Confirm.js";

const useStyles = makeStyles((theme) => ({
    root: {
      height: "100vh",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      "& > *": {
        margin: theme.spacing(1)
      }
    }
  }));

const Typeform = ({ children, onSubmit }) => {
    const classes = useStyles();
    children = [...children, <div></div>];
    const [fields, setFields] = useState(0);
    const nextField = () => {
      if ((fields < children.length) && (children[fields])) setFields((prev) => prev + 1);

      if (fields === children.length - 2) {
        onSubmit();
      }
    };
    const prevField = () => {
      if (fields > 0) setFields((prev) => prev - 1);
    };

  return (

      <form className={classes.box} onSubmit={onSubmit}>
          {children[fields]}
          <div className='flex justify-center'>
            <ButtonGroup
            disableElevation
            size="large"
            variant="contained"
            color="primary"
            >
              {fields < children.length - 1 && fields > 0 && (
                
                <Button onClick={prevField} className='m-2'>back</Button>
              )}
              {fields < children.length - 2 && (
                <Button onClick={nextField} className='m-2'>Next</Button>
              )}
              {fields === children.length - 2 && (
                <Button onClick={nextField} className='m-2'>Submit</Button>
              )}
            </ButtonGroup>
          </div>
    </form>

  )
}

export default Typeform