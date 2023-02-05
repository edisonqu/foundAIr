import { Parallax } from 'react-parallax';
import moon from "../images/moon.png"
const imageTwo = () => (
    <div>
    <Parallax className='images' bgImage={moon} strength={800}>
    </Parallax>
    </div>
);

export default imageTwo