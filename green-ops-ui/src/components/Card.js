import * as React from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Typography from "@mui/material/Typography";
import { CardActionArea } from "@mui/material";

const AreaCard = ({ name, temp, colors, count }) => {
  return (
    <Card sx={{ maxWidth: 345, minHeight: 200, margin: 2 }}>
      <CardActionArea>
        <div
          style={{
            height: "140px",
            background: temp>30 ? "red" : temp>25 ? "orange" : 20<temp<25 ? "green": "red",

          }}
        />
        <CardContent>
          <Typography gutterBottom variant="h5"  component="div">
            Area: <b>{name}</b>
          </Typography>
          {/* <Typography variant="h6" color="text.secondary" s>
            Current temprature of this area is {temp || "20 "} *C
          </Typography> */}
          <Typography variant="h5" >
           People inside <b>{count}</b>
          </Typography>
          {/* <Typography variant="h6" color="text.secondary" s>
           Temprature per person {20}
          </Typography>
          <Typography variant="h6" color="text.secondary" s>
           Enviroment temprature {20}
          </Typography>
          <Typography variant="h6" color="text.secondary" s>
           Suggested AC temprature {20}
          </Typography>
          <Typography variant="h6" color="text.secondary" s>
           Suggested formula {"e = mc2"}
          </Typography> */}
        </CardContent>
      </CardActionArea>
    </Card>
  );
};
export default AreaCard;
