package LibTest;

import LibNet.NetLibrary;
import PetriObj.*;
import java.util.ArrayList;

public class Task2 {

    public static void main(String[] args) throws
            ExceptionInvalidTimeDelay, ExceptionInvalidNetStructure {
        PetriObjModel model = getModel();
        model.setIsProtokol(false);
        model.go(10000);
        System.out.println("Total details: " + countTotalDetails(model));
    }

    private static int countTotalDetails(PetriObjModel model) {
        return model.getListObj().get(5).getNet().getListP()[5].getMark();
    }

    public static PetriObjModel getModel() throws
            ExceptionInvalidNetStructure, ExceptionInvalidTimeDelay {
        ArrayList<PetriSim> list = new ArrayList<>();
        
//        створення підмоделей
        list.add(new PetriSim(NetLibrary.CreateNetGenerator(40.0)));    // генератор
        list.add(new PetriSim(mover(6)));                              // робот1
        list.add(new PetriSim(processor(60, "norm")));        // верстат1
        list.add(new PetriSim(mover(7)));                              // робот2
        list.add(new PetriSim(processor(100, "exp")));        // верстат2
        list.add(new PetriSim(mover(5)));                              // робот3
        
//        зв'язання моделей
        list.get(0).getNet().getListP()[1] = list.get(1).getNet().getListP()[4]; // генератор -> робот1
        list.get(1).getNet().getListP()[5] = list.get(2).getNet().getListP()[1]; // робот1 -> верстат1
        list.get(2).getNet().getListP()[2] = list.get(3).getNet().getListP()[4]; // верстат1 -> робот2
        list.get(3).getNet().getListP()[5] = list.get(4).getNet().getListP()[1]; // робот2 -> верстат2
        list.get(4).getNet().getListP()[2] = list.get(5).getNet().getListP()[4]; // верстат2 -> робот3
        
        return new PetriObjModel(list);
    }

    private static PetriNet mover(double timeMean)
            throws ExceptionInvalidTimeDelay {
        
        ArrayList<PetriP> places = new ArrayList<>();
        places.add(new PetriP("availableRobot", 1));
        places.add(new PetriP("finishedDeliver", 0));
        places.add(new PetriP("pickedUp", 0));
        places.add(new PetriP("finishedMoving", 0));
        places.add(new PetriP("availableDetails", 0));
        places.add(new PetriP("delivered", 0));
        
        ArrayList<PetriT> transitions = new ArrayList<>();
        transitions.add(new PetriT("pickUp", 8.0));
        transitions.get(0).setDistribution("norm", transitions.get(0).getTimeServ());
        transitions.get(0).setParamDeviation(1.0);
        transitions.add(new PetriT("moveBack", timeMean));
        transitions.add(new PetriT("releaseDetail", 8.0));
        transitions.get(2).setDistribution("norm", transitions.get(2).getTimeServ());
        transitions.get(2).setParamDeviation(1.0);
        transitions.add(new PetriT("moveDetail", 6.0));
        
        ArrayList<ArcIn> arcIns = new ArrayList<>();
        ArrayList<ArcOut> arcOuts = new ArrayList<>();
        arcIns.add(new ArcIn(places.get(0), transitions.get(0), 1));
        arcIns.add(new ArcIn(places.get(1), transitions.get(1), 1));
        arcIns.add(new ArcIn(places.get(2), transitions.get(3), 1));
        arcIns.add(new ArcIn(places.get(3), transitions.get(2), 1));
        arcIns.add(new ArcIn(places.get(4), transitions.get(0), 1));
        arcOuts.add(new ArcOut(transitions.get(1), places.get(0), 1));
        arcOuts.add(new ArcOut(transitions.get(0), places.get(2), 1));
        arcOuts.add(new ArcOut(transitions.get(2), places.get(1), 1));
        arcOuts.add(new ArcOut(transitions.get(3), places.get(3), 1));
        arcOuts.add(new ArcOut(transitions.get(2), places.get(5), 1));
        
        PetriNet petriNet = new PetriNet("mover", places, transitions, arcIns, arcOuts);
        PetriP.initNext();
        PetriT.initNext();
        ArcIn.initNext();
        ArcOut.initNext();
        return petriNet;
    }

    private static PetriNet processor(double timeMean, String distribution)
            throws ExceptionInvalidTimeDelay {
        
        ArrayList<PetriP> places = new ArrayList<>();
        places.add(new PetriP("workers", 3));
        places.add(new PetriP("details", 0));
        places.add(new PetriP("completed", 0));
        
        ArrayList<PetriT> transitions = new ArrayList<>();
        transitions.add(new PetriT("process", timeMean));
        transitions.get(0).setDistribution(distribution, transitions.get(0).getTimeServ());
        transitions.get(0).setParamDeviation(10.0);
        
        ArrayList<ArcIn> arcIns = new ArrayList<>();
        ArrayList<ArcOut> arcOuts = new ArrayList<>();
        arcIns.add(new ArcIn(places.get(0), transitions.get(0), 1));
        arcIns.add(new ArcIn(places.get(1), transitions.get(0), 1));
        arcOuts.add(new ArcOut(transitions.get(0), places.get(0), 1));
        arcOuts.add(new ArcOut(transitions.get(0), places.get(2), 1));
        
        PetriNet petriNet = new PetriNet("processor", places, transitions, arcIns, arcOuts);
        PetriP.initNext();
        PetriT.initNext();
        ArcIn.initNext();
        ArcOut.initNext();
        return petriNet;
    }
}