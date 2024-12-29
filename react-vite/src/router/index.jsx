import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/Login/LoginFormPage';
import SignupFormPage from '../components/Signup/SignupFormPage';
import UserProfile from '../components/User/UserProfile/UserProfile';
import ArtifactDetails from '../components/Artifacts/ArtifactDetails/ArtifactDetails';
import PromptDetails from '../components/Prompts/PromptDetails/PromptDetails';
import ArtifactForm from '../components/Artifacts/Artifactform/ArtifactForm';
import ArticleForm from '../components/Articles/ArticleForm/ArticleForm';
import PromptForm from '../components/Prompts/PromptForm/PromptForm';
import ArticleDetails from '../components/Articles/ArticleDetails/ArticleDetails';
import ArtifactPage from '../components/Artifacts/ArtifactPage/ArtifactPage';
import ArticlePage from '../components/Articles/ArticlePage/ArticlePage';
import PromptPage from '../components/Prompts/PromptPage/PromptPage';
import Homepage from '../components/Home/Homepage';
import SearchResults from '../components/Search/SearchResults';
import Layout from './Layout';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <Homepage />,
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
        path: "searchEngine/:query",
        element: <SearchResults />
      },
      {
        path: "documents",
        children: [
          {
            path: "all",
            element: <ArtifactPage />,
          },
          {
            path: ":id",
            element: <ArtifactDetails />
          },
          {
            path: "form",
            element: <ArtifactForm />
          },
        ]
      },
      {
        path: "prompts",
        children: [
          {
            path: "all",
            element: <PromptPage/>
          },
          {
            path: ":id",
            element: <PromptDetails />
          },
          {
            path: "form",
            element: <PromptForm />
          }
        ]
      },
      {
        path: "articles",
        children: [
          {
            path: "all",
            element: <ArticlePage />,
          },
          {
            path: ":id",
            element: <ArticleDetails />
          },
          {
            path: "form",
            element: <ArticleForm />
          }
        ]
      }
    ],
  },
]);