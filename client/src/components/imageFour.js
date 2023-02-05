import { Parallax } from 'react-parallax';
import mountainsfront from "../images/mountains_front.png"
const ImageFour = () => (
    <div className='text-box'>
    <Parallax className='images' bgImage={mountainsfront} strength={800}>
        <div className="content">
            <span className="img-txt">a trip to space </span>
        </div>
    </Parallax>
    </div>
);

export default ImageFour

