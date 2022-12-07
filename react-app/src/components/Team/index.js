import "./team.css"
import mainLogo from "../../assets/main-logo-2.png"
import githubLogo from "../../assets/github-logo.svg"
import linkedinLogo from "../../assets/linkedin-logo.png"
import profilePic1 from "../../assets/profile-pic-1.png"
import profilePic2 from "../../assets/profile-pic-2.png"
import profilePic3 from "../../assets/profile-pic-3.png"
import { useHistory } from "react-router-dom"
import { useSelector } from "react-redux"
import NavBar from "../NavBar"

const Team = () => {
    const history = useHistory()
    const user = useSelector(state => state.session.user)
    const goHome = () => {
        history.push("/")
    }



    return (
        <div id="team-container">


            <div id="team-header">
                <div id="team-header-2">
                    <img className="cursor" onClick={goHome} src={mainLogo} width="36px" height="36px" />
                    <div className="cursor" onClick={goHome} id="go-back-home">Go Back Home</div>
                </div>
            </div>


            <div id="team-body">
                <div id="team-body-header">The Median Team</div>
                <div id="three-people">

                    <div className="individual">
                        <img src={profilePic1} width="200px" height="200px" />

                        <div className="individual-name">
                            Calvin Tzeng
                        </div>
                        <div className="individual-title">
                            Team Lead
                        </div>
                        <div className="linkedin-github">
                            <a href="//github.com/calvintzeng96">
                                <img src={githubLogo} width="60px" height="60px" />
                            </a>
                            <a href="//linkedin.com/in/calvintzengviolins">
                                <img src={linkedinLogo} width="60px" height="60px" />
                            </a>
                        </div>
                    </div>




                    <div className="individual">
                        <img src={profilePic2} width="200px" height="200px" />

                        <div className="individual-name">
                            Alex Feinberg
                        </div>
                        <div className="individual-title">
                            Frontend Lead
                        </div>
                        <div className="linkedin-github">
                            <a href="//github.com/alexanderfeinberg">
                                <img src={githubLogo} width="60px" height="60px" />
                            </a>
                            <a href="//linkedin.com/in/alex-feinberg/">
                                <img src={linkedinLogo} width="60px" height="60px" />
                            </a>
                        </div>
                    </div>




                    <div className="individual">
                        <img src={profilePic3} width="200px" height="200px" />

                        <div className="individual-name">
                            Jenny Jiang
                        </div>
                        <div className="individual-title">
                            Backend Lead
                        </div>
                        <div className="linkedin-github">
                            <a href="//github.com/jenjenkayi">
                                <img src={githubLogo} width="60px" height="60px" />
                            </a>
                            <a href="//linkedin.com/in/jenny-jiang-81033b48/">
                                <img src={linkedinLogo} width="60px" height="60px" />
                            </a>


                        </div>
                    </div>
                </div>
            </div>
        </div >

    )
}

export default Team
