import React, { useState } from 'react';
import Header from './Header';
import UploadForm from './UploadForm';
import Result from './Result';
import './App.css';

const App = () => {
  const [result, setResult] = useState(null);

  return (
    <div className="App">
      <Header />
      <main>
        <UploadForm setResult={setResult} />
        <Result result={result} />
      </main>
    </div>
  );
};

export default App;
