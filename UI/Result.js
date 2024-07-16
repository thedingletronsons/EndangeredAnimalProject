import React from 'react';

const Result = ({ result }) => {
  return (
    <div>
      {result ? (
        <div>
          <h2>Recognition Result:</h2>
          <p>Species: {result.species}</p>
          <p>Confidence: {result.confidence}</p>
        </div>
      ) : (
        <p>No result yet</p>
      )}
    </div>
  );
};

export default Result;
