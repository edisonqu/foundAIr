import { Parallax } from 'react-parallax';
import moon from "../img/moon.png"
const imageTwo = () => (
    <div>
    <Parallax className='image' bgImage={moon} strength={800}>
    </Parallax>
    </div>
);

export default imageTwo