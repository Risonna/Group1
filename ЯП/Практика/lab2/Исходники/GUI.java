import java.awt.*;
import java.awt.event.*;

class MyWindowAdapter extends WindowAdapter
{
   Frame fFrame;	
   public MyWindowAdapter(Frame f)
   {
	   fFrame = f;
   }   
   
   public void windowClosing(WindowEvent we)
   {
	   System.out.println("Closing window...");
	   fFrame.setVisible(false);
	   System.out.println("Exiting system...");	   
	   System.exit(0);
   }
}

class MyActionListener implements ActionListener
{
	MyFrame fFrame;
	public MyActionListener(MyFrame f)
	{
		fFrame = f;
	}
	
	public void actionPerformed(ActionEvent e)
	{
	  int delta = fFrame.fCanvas.getDelta();	
	  fFrame.fCanvas.setDelta(delta+10);
	  fFrame.fCanvas.repaint();
	}
}


class MyCanvas extends Canvas
{
	int delta;
	
	public MyCanvas() { delta=0; }
	
	public void setDelta(int d) { delta = d; }
	public int getDelta() { return delta; }
	
	public void paint(Graphics g)
	{
	   System.out.println("Painting...");	
	   g.drawRect(10,10,20+delta,20+delta); 
	}
}

class MyFrame extends Frame
{
	private Panel fPanel;	
	
	private Button fButtonW;
	private Button fButtonE;
	private Button fButtonN;
	private Button fButtonS;
	
	public MyCanvas fCanvas;
	
	public MyFrame()
	{		
		fPanel = new Panel();						
		add(fPanel);
		
		fPanel.setLayout(new BorderLayout());
		
		fButtonW = new Button("W");
		fButtonW.addActionListener(new MyActionListener(this));				
		fPanel.add(fButtonW,BorderLayout.WEST);
		
		fButtonE = new Button("E");		
		fPanel.add(fButtonE,BorderLayout.EAST);
		
		fButtonN = new Button("N");		
		fPanel.add(fButtonN,BorderLayout.NORTH);
		
		fButtonS = new Button("S");		
		fPanel.add(fButtonS,BorderLayout.SOUTH);
		
		fCanvas = new MyCanvas();
		fPanel.add(fCanvas,BorderLayout.CENTER);
						
		addWindowListener(new MyWindowAdapter(this));
	}
}



class GUI
{
	public static void main(String args[])
	{		
		MyFrame f = new MyFrame();
		f.setTitle("My first window application");
		f.setSize(500,500);
		f.setVisible(true);	

                String enIn =  "Cp1251";
                String enOut = "Cp1251";


                String s = "End. Конец.";

                try
                {
                  System.out.println(s);
                  System.out.println( new String(s.getBytes(enIn),enOut) );
                }
                catch (Exception e) {} 
	
		System.out.println("Ending main...");
	}
}

