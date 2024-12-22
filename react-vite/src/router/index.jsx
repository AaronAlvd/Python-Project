import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/Login/LoginFormPage';
import SignupFormPage from '../components/Signup/SignupFormPage';
import UserProfile from '../components/User/UserProfile/UserProfile';
import ArtifactDetails from '../components/Artifacts/ArtifactDetails/ArtifactDetails';
import PromptDetails from '../components/Prompts/PromptDetails';
import ArtifactForm from '../components/Artifacts/Artifactform/ArtifactForm';
import Layout from './Layout';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <h1>Welcome!</h1>,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "profile",
        element: <UserProfile />
      },
      {
        path: "transcription",
        children: [
          {
            path: ":id",
            element: <ArtifactDetails />
          },
          {
            path: "form",
            element: <ArtifactForm />
          }
        ]
      },
      {
        path: "prompt",
        children: [
          {
            path: ":id",
            element: <PromptDetails />
          },
          {
            path: "form",
          }
        ]
      }
    ],
  },
]);