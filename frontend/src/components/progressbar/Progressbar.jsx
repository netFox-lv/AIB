import "./progressbar.scss"
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import { CircularProgressbarWithChildren } from 'react-circular-progressbar';
const percentage = 23;

const Progressbar = () => {
  return (
    <div className="progressbar">
      <div className="top">
        <h3 className="title">Statistics</h3>
        <div className="subtitle">This year</div>
      </div>  
      <div className="featchart">
        <CircularProgressbar value={percentage} text={`$23,600`} 
        styles={buildStyles({
            // Whether to use rounded or flat corners on the ends - can use 'butt' or 'round'
            strokeLinecap: 'butt',

            // Text size
            textSize: '16px',

            // Colors
            pathColor: `#3751FF`,
            textColor: '#252733',
            trailColor: '#F0F2FF',
            backgroundColor: '#3751FF',
          })}
        />
      </div>
      <div className="bottom"> 
        <div className="section">
          <p className="amount">$96,850</p>
          <p className="name">Earned</p>
        </div>
        <div className="section">
          <p className="amount">$73,250</p>
          <p className="name">Remaining</p>  
        </div>
      </div>
    </div>
  )
}

export default Progressbar