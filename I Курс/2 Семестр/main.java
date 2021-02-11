import java.lang.Math;

class practice {
	public static void main(String[] args) {
		YellowBalloonClass Balloon = new YellowBalloonClass();
		Balloon.changeHeight(1000);
	}
}

abstract class DefaultBalloon
{
	void turnFireOn() {
	}

	void turnFireOff() {
	}

	void putPassengersOnBalloon(int amount) {
	}

	void changeHeight(double newHeight) {
	}

	String balloonState() {
		return "";
	}

	void setPathLength(double newPathLength) {
	}

	String getPathLength() {
		return "";
	}
}

class YellowBalloonClass extends DefaultBalloon {
	private double height = 0;
	private double pathLength = 0;
	private int passengers = 0;
	private boolean fireState = false;

	@Override
	void turnFireOn() {
		try {
			if (height == 0) {
				fireState = true;
			} else {
				throw new Exception("");
			}
		} catch (Exception e) {
			ExceptionManager(e);
		}
	}

	void turnFireOff() {
		try {
			if (height == 0) {
				fireState = false;
			} else {
				throw new Exception("You can't turn the fire off while being in mid-air");
			}
		} catch (Exception e) {
			ExceptionManager(e);
		}
	}

	void putPassengersOnBalloon(int amount) {
		try {
			if (height != 0 & fireState == true) {
				throw new Exception("You can't let anyone in while being in mid-air");
			} else if (amount > 10) {
				throw new Exception("Maximum capacity of the balloon is 10 people");
			} else if (amount < 0) {
				throw new Exception("Amoun of passengers can't be negative");
			} else {
				passengers = amount;
			}
		} catch (Exception e) {
			ExceptionManager(e);
		}
	}

	void changeHeight(double newHeight) {
		try {
			if (fireState == false) {
				throw new Exception("You can't change height while being on the ground");
			} else if (newHeight > 5000) {
				throw new Exception("Maximum possible height is 5000m");
			} else if (newHeight < 0) {
				throw new Exception("Minimum possible height is 0m");
			} else {
				height = newHeight;
			}
		} catch (Exception e) {
			ExceptionManager(e);
		}
	}

	String balloonState() {
		return "Current height is "+height+"m and current passenger count is "+passengers;
	}

	void setPathLength(double newPathLength) {
		try {
			if (fireState == false) {
				throw new Exception("You can't change path length while being on the ground");
			} else if (newPathLength < pathLength) {
				throw new Exception("New path length should be bigger than previous");
			} else {
				pathLength = newPathLength;
			}
		} catch (Exception e) {
			ExceptionManager(e);
		}
	}

	String getPathLength() {
		if (fireState == false) {
			return "We are still on the ground";
		} else {
			return "The balloon flew "+pathLength+"m";
		}
	}

	private void ExceptionManager(Exception e) {
		System.out.println(e.getMessage());
	}
}