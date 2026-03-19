import { useState } from "react";
import "./App.css";
import RegisterPage from "./RegisterPage";
import { LoginPage } from "./LoginPage";
import JobListPage from "./JobListPage";
import { ApplyJob } from "./ApplyJob";
import { BrowserRouter, Route, Routes } from "react-router-dom";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      {/* <RegisterPage /> */}
      {/* <LoginPage /> */}
      {/* <JobListPage /> */}
      {/* <ApplyJob /> */}

      <BrowserRouter>
        <Routes>
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/jobs" element={<JobListPage />} />
          <Route path="/apply/:jobId" element={<ApplyJob />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
