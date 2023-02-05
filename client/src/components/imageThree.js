import { Parallax } from 'react-parallax';
import mountainsbehind from "../img/mountains_behind.png"
const imageThree = () => (
    <div>
    <Parallax className='image' bgImage={mountainsbehind} strength={800}>
        <div className="content">
            <span className="img-txt">a trip to space </span>
        </div>
    </Parallax>
    </div>
);

export default imageThree