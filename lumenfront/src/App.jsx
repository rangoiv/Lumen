import React, { useState, useEffect } from 'react';

import FrontPage from './FrontPage';
import About from './About';
import "./styles/Wrapper.css"
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import KeyboardVoiceIcon from '@mui/icons-material/KeyboardVoice';
import InfoIcon from '@mui/icons-material/Info';
import HomeIcon from '@mui/icons-material/Home';
import { Container } from '@mui/material';
import Record from './Record';

const App = () => {
	const [activePage, setActivePage] = useState(1);

	useEffect(() => {
		const handleKeyPress = (event) => {
			if (event.code === 'ArrowLeft') {
				if (activePage === 0) setActivePage(2)
				else
					setActivePage(activePage-1);
			}
			if (event.code === 'ArrowRight') {
				setActivePage((activePage+1) % 3);
			}
		};
  
		window.addEventListener('keydown', handleKeyPress);
  
		return () => {
			window.removeEventListener('keydown', handleKeyPress);
		};
	}, [activePage]);
  
	const handleDotClick = (index) => {
		setActivePage(index);
	};
  
	const handleSwipe = (event) => {
	    const deltaX = event.deltaX;
	    if (deltaX > 0) {
	        if (activePage === 0) setActivePage(2)
			else
				setActivePage(activePage-1);
	    } else if (deltaX < 0) {
	        setActivePage((activePage+1) % 3);
	    }
	};

	const handleDotKeyDown = (event, index) => {
		if (event.code === 'Enter' || event.code === 'Space') {
			setActivePage(index);
		}
	};
  
	const handleDotKeyUp = (event) => {
		event.preventDefault();
	};

	function DotsContainer() {
		return(
			<div className='parent'>
				<div className="dotsContainer">
					{[0,1,2].map((index) => {
						return (
							<div
								key={index}
								className="dot"
								style={index === activePage ? {opacity: 1} : {opacity: 0.5}}
								tabIndex="0"
								role="button"
								onClick={() => handleDotClick(index)}
								onKeyDown={(event) => handleDotKeyDown(event, index)}
								onKeyUp={handleDotKeyUp}
							/>
						);
					})}
				</div>
			</div>
		)
	}

	function Header() {
		switch(activePage){
			case 0: return(
				<BottomNavigation showLabels value={activePage} onChange={(event, newValue) => { setActivePage(1); }} style={{backgroundColor: 'inherit', width: '100%'}} >
					<BottomNavigationAction label="Record" icon={<KeyboardVoiceIcon />} disabled style={{ color: 'white' }}/>
					<DotsContainer/>
					<BottomNavigationAction label="Nearby" icon={<HomeIcon />} />
				</BottomNavigation>
			)
			case 1: return(
				<BottomNavigation showLabels value={activePage} onChange={(event, newValue) => { setActivePage(newValue); }} style={{backgroundColor: 'inherit', width: '100%'}} >
					<BottomNavigationAction label="Record" icon={<KeyboardVoiceIcon />} />
					<DotsContainer/>
					<BottomNavigationAction label="About us" icon={<InfoIcon />} />
				</BottomNavigation>
			)
			case 2: return(
				<BottomNavigation showLabels value={activePage} onChange={(event, newValue) => { setActivePage(1); }} style={{backgroundColor: 'inherit', width: '100%'}} >
					<BottomNavigationAction label="Home" icon={<HomeIcon />} />
					<DotsContainer/>
					<BottomNavigationAction label="About us" icon={<InfoIcon />} disabled style={{ color: 'white' }} />
				</BottomNavigation>
			)
		}
	}

	function Page() {
		switch(activePage){
			case 0: return(<Record />)
			case 1: return(<FrontPage />)
			case 2: return(<About />)
		}
	}

	return (
		<div>
			<div className="header">
				<Header/>
			</div>
			<div className="page">
				<Page/>
			</div>
			
		</div>
	);
};

export default App;