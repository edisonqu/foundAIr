import { Parallax } from 'react-parallax';
import mountainsfront from "../img/mountains_front.png"
const imageFour = () => (
    <div>
    <Parallax className='image' bgImage={mountainsfront} strength={800}>
        <div className="content">
            <span className="img-txt">a trip to space </span>
        </div>
    </Parallax>
    </div>
);

export default imageFour