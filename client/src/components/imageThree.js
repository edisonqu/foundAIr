import { Parallax } from 'react-parallax';
import mountainsbehind from "../images/mountains_behind.png"
const imageThree = () => (
    <div>
    <Parallax className='images' bgImage={mountainsbehind} strength={800}>
        <div className="content">
            <span className="img-txt">a trip to space </span>
        </div>
    </Parallax>
    </div>
);

export default imageThree