import React from "react";
import Stack from "@mui/material/Stack";
import Paper from "@mui/material/Paper";
import { styled } from "@mui/material/styles";

const DetailArea = () => {
  const DemoPaper = styled(Paper)(({ theme }) => ({
    width: 120,
    height: 120,
    padding: theme.spacing(2),
    ...theme.typography.h6,
    textAlign: "center",
    backgroundColor:"grey"
  }));
  return (
    <>
      
      <div style={{ display: "inline-flex", gap: "2rem", margin: "2rem"}}>
     
        <Stack direction="row" spacing={2}>
        Going_in:<DemoPaper square={false} > 16</DemoPaper>
        <DemoPaper square>Going_out: 10</DemoPaper>
      </Stack>
      </div>
    </>
  );
};

export default DetailArea;
