import { Parallax } from 'react-parallax';
import stars from "../img/stars.png"
const ImageOne = () => (
    <div>
    <Parallax className='image' bgImage={stars} strength={800}>
        <div className="content">
            <span className="img-txt">a trip to space </span>
        </div>
    </Parallax>
    </div>
);

export default ImageOne
