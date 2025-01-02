import { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { ModalProvider, Modal } from "../context/Modal";
import { thunkAuthenticate } from "../redux/session";
import Navigation from "../components/Navigation/Navigation";
import Default from '../components/Default/default';

export default function Layout() {
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user)
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(thunkAuthenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <ModalProvider>
        <Navigation />
        {(user === null) ? <Default /> : (isLoaded && <Outlet />)}
        <Modal />
      </ModalProvider>
    </>
  );
}
