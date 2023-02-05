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
    children = [...children, <Confirm />];
    const [fields, setFields] = useState(0);
    const nextField = () => {
      if ((fields < children.length) && (children[fields])) setFields((prev) => prev + 1);
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
                <Button onClick={nextField} className='mx-12'>Next</Button>
              )}
              {fields === children.length - 2 && (
                <input
                type="submit"
                className="rounded-xl p-4 text-white bg-zinc-800 active:bg-zinc-600 transition-all duration-75 font-bold cursor-pointer px-36 py-8"
                value="Submit"

            />
              )}
            </ButtonGroup>
          </div>
    </form>

  )
}

export default Typeform